from typing import Optional

from django.db import models

import pledges.models as pledges_models


class ActionType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Action(models.Model):
    version = models.IntegerField()
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    _VERSIONS = {}

    def get_text(self, pledge) -> str:
        self._check_version()
        raise NotImplementedError

    def get_co2(self, pledge) -> Optional[float]:
        self._check_version()
        return None

    def get_water(self, pledge) -> Optional[float]:
        self._check_version()
        return None

    def get_waste(self, pledge) -> Optional[float]:
        self._check_version()
        return None

    def _check_version(self):
        if self.version not in self.__class__._VERSIONS:
            raise NotImplementedError


class VegOutAction(Action):
    _VERSIONS = {0}

    def get_text(self, pledge: pledges_models.VegOutPledge) -> str:
        self._check_version()
        return (
            f"At the moment, I munch on {pledge.current_meals} meaty meals each week. For the next two months, "
            f"I pledge to go veg for {pledge.veggie_meals.label} extra meals each week."
        )

    def get_co2(self, pledge: pledges_models.VegOutPledge) -> float:
        self._check_version()
        return 0.884 * self._get_veggie_meals_value(pledge.veggie_meals) * 8.7

    def get_water(self, pledge: pledges_models.VegOutPledge) -> float:
        self._check_version()
        return 0.75 * pledge.current_meals

    def get_waste(self, pledge: pledges_models.VegOutPledge) -> float:
        self._check_version()
        return 0.2 * pledge.current_meals * self._get_veggie_meals_value(pledge.veggie_meals)

    def _get_veggie_meals_value(self, veggie_meals: pledges_models.VegOutVeggieMeals) -> float:
        self._check_version()
        return {
            pledges_models.VegOutVeggieMeals.ZERO_TO_FIVE: 2.5,
            pledges_models.VegOutVeggieMeals.SIX_PLUS: 3,
        }.get(veggie_meals)


class CleanYourBillsActions(Action):
    _VERSIONS = {0}

    def get_text(self, pledge: pledges_models.CleanYourBillsPledge) -> str:
        self._check_version()
        return (
            f"Within the next two months, I pledge to switch from my current energy supplier – which is "
            f"{pledge.energy_supplier.label} – to a green energy supplier. {pledge.number_of_people} people live in "
            f"our home. My house is mainly heated by {pledge.heating_source.label}."
        )

    def get_co2(self, pledge: pledges_models.CleanYourBillsPledge) -> float:
        self._check_version()
        return (
            49
            * self._get_energy_supplier_value(pledge.energy_supplier)
            * pledge.number_of_people
            * self._get_heating_source_value(pledge.heating_source)
        )

    def _get_energy_supplier_value(self, energy_supplier: pledges_models.CleanYourBillsEnergySupplier) -> float:
        self._check_version()
        return {
            pledges_models.CleanYourBillsEnergySupplier.STANDARD: 0.5,
            pledges_models.CleanYourBillsEnergySupplier.GREEN: 0,
        }.get(energy_supplier)

    def _get_heating_source_value(self, heating_source: pledges_models.CleanYourBillsHeatingSource) -> float:
        self._check_version()
        return {
            pledges_models.CleanYourBillsHeatingSource.GAS_OR_OIL: 5,
            pledges_models.CleanYourBillsHeatingSource.ELECTRICITY: 3,
        }.get(heating_source)
