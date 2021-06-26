from django.contrib.auth.models import User

from django.db import models


class VegOutVeggieMeals(models.TextChoices):
    ZERO_TO_FIVE = "05", "0-5"
    SIX_PLUS = "6P", "6+"


class CleanYourBillsEnergySupplier(models.TextChoices):
    STANDARD = "BS", "bog standard"
    GREEN = "GG", "a great green tariff"


class CleanYourBillsHeatingSource(models.TextChoices):
    GAS_OR_OIL = "GO", "gas or oil"
    ELECTRICITY = "EC", "electricity"


class Pledge(models.Model):
    _ACTION_MODEL = None

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def on_class_prepared(cls):
        target_field = models.ForeignKey(cls._ACTION_MODEL, on_delete=models.CASCADE)
        target_field.contribute_to_class(cls, "action")

    class Meta:
        abstract = True

    def display_name(self):
        return self.action.action_type.name


class VegOutPledge(Pledge):
    _ACTION_MODEL = "actions.VegOutAction"

    current_meals = models.IntegerField()
    veggie_meals = models.CharField(
        max_length=2,
        choices=VegOutVeggieMeals.choices,
    )


class CleanYourBillsPledge(Pledge):
    _ACTION_MODEL = "actions.CleanYourBillsActions"

    energy_supplier = models.CharField(
        max_length=2,
        choices=CleanYourBillsEnergySupplier.choices,
    )
    number_of_people = models.IntegerField()
    heating_source = models.CharField(
        max_length=2,
        choices=CleanYourBillsHeatingSource.choices,
    )
