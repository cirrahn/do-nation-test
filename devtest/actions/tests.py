from django.test import TestCase
import pledges.models as pledges_models
import actions.models as actions_models


class _Utils:
    @staticmethod
    def test_invalid_version(test_case: TestCase, action: actions_models.Action):
        with test_case.assertRaises(NotImplementedError):
            action.get_text(...)
        with test_case.assertRaises(NotImplementedError):
            action.get_co2(...)
        with test_case.assertRaises(NotImplementedError):
            action.get_water(...)
        with test_case.assertRaises(NotImplementedError):
            action.get_waste(...)


class TestVegOutAction(TestCase):
    _ACTION = actions_models.VegOutAction(version=0)
    _PLEDGE_0 = pledges_models.VegOutPledge(current_meals=0, veggie_meals=pledges_models.VegOutVeggieMeals.ZERO_TO_FIVE)
    _PLEDGE_1 = pledges_models.VegOutPledge(current_meals=5, veggie_meals=pledges_models.VegOutVeggieMeals.SIX_PLUS)
    _PLEDGE_2 = pledges_models.VegOutPledge(current_meals=5, veggie_meals=pledges_models.VegOutVeggieMeals.ZERO_TO_FIVE)

    def test_metrics(self):
        self.assertAlmostEqual(TestVegOutAction._ACTION.get_co2(TestVegOutAction._PLEDGE_0), 19.227)
        self.assertEqual(TestVegOutAction._ACTION.get_water(TestVegOutAction._PLEDGE_0), 0)
        self.assertEqual(TestVegOutAction._ACTION.get_waste(TestVegOutAction._PLEDGE_0), 0)

        self.assertAlmostEqual(TestVegOutAction._ACTION.get_co2(TestVegOutAction._PLEDGE_1), 23.0724)
        self.assertEqual(TestVegOutAction._ACTION.get_water(TestVegOutAction._PLEDGE_1), 3.75)
        self.assertEqual(TestVegOutAction._ACTION.get_waste(TestVegOutAction._PLEDGE_1), 3.0)

        self.assertAlmostEqual(TestVegOutAction._ACTION.get_co2(TestVegOutAction._PLEDGE_2), 19.227)
        self.assertEqual(TestVegOutAction._ACTION.get_water(TestVegOutAction._PLEDGE_2), 3.75)
        self.assertEqual(TestVegOutAction._ACTION.get_waste(TestVegOutAction._PLEDGE_2), 2.5)

    def test_invalid_version(self):
        action = actions_models.VegOutAction(version=-1)
        _Utils.test_invalid_version(self, action)

    def test_text(self):
        self.assertEqual(
            TestVegOutAction._ACTION.get_text(TestVegOutAction._PLEDGE_0),
            "At the moment, I munch on 0 meaty meals each week. For the next two months, I pledge to go veg for 0-5 extra meals each week.",
        )
        self.assertEqual(
            TestVegOutAction._ACTION.get_text(TestVegOutAction._PLEDGE_1),
            "At the moment, I munch on 5 meaty meals each week. For the next two months, I pledge to go veg for 6+ extra meals each week.",
        )
        self.assertEqual(
            TestVegOutAction._ACTION.get_text(TestVegOutAction._PLEDGE_2),
            "At the moment, I munch on 5 meaty meals each week. For the next two months, I pledge to go veg for 0-5 extra meals each week.",
        )


class TestCleanYourBillsActions(TestCase):
    _ACTION = actions_models.CleanYourBillsActions(version=0)
    _PLEDGE_0 = pledges_models.CleanYourBillsPledge(
        energy_supplier=pledges_models.CleanYourBillsEnergySupplier.GREEN,
        number_of_people=2,
        heating_source=pledges_models.CleanYourBillsHeatingSource.GAS_OR_OIL,
    )
    _PLEDGE_1 = pledges_models.CleanYourBillsPledge(
        energy_supplier=pledges_models.CleanYourBillsEnergySupplier.STANDARD,
        number_of_people=2,
        heating_source=pledges_models.CleanYourBillsHeatingSource.GAS_OR_OIL,
    )
    _PLEDGE_2 = pledges_models.CleanYourBillsPledge(
        energy_supplier=pledges_models.CleanYourBillsEnergySupplier.GREEN,
        number_of_people=2,
        heating_source=pledges_models.CleanYourBillsHeatingSource.ELECTRICITY,
    )
    _PLEDGE_3 = pledges_models.CleanYourBillsPledge(
        energy_supplier=pledges_models.CleanYourBillsEnergySupplier.STANDARD,
        number_of_people=2,
        heating_source=pledges_models.CleanYourBillsHeatingSource.ELECTRICITY,
    )

    def test_metrics(self):
        self.assertAlmostEqual(TestCleanYourBillsActions._ACTION.get_co2(TestCleanYourBillsActions._PLEDGE_0), 0)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_water(TestCleanYourBillsActions._PLEDGE_0), None)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_waste(TestCleanYourBillsActions._PLEDGE_0), None)

        self.assertAlmostEqual(TestCleanYourBillsActions._ACTION.get_co2(TestCleanYourBillsActions._PLEDGE_1), 245.0)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_water(TestCleanYourBillsActions._PLEDGE_1), None)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_waste(TestCleanYourBillsActions._PLEDGE_1), None)

        self.assertAlmostEqual(TestCleanYourBillsActions._ACTION.get_co2(TestCleanYourBillsActions._PLEDGE_2), 0)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_water(TestCleanYourBillsActions._PLEDGE_2), None)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_waste(TestCleanYourBillsActions._PLEDGE_2), None)

        self.assertAlmostEqual(TestCleanYourBillsActions._ACTION.get_co2(TestCleanYourBillsActions._PLEDGE_3), 147.0)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_water(TestCleanYourBillsActions._PLEDGE_3), None)
        self.assertEqual(TestCleanYourBillsActions._ACTION.get_waste(TestCleanYourBillsActions._PLEDGE_3), None)

    def test_text(self):
        self.assertEqual(
            TestCleanYourBillsActions._ACTION.get_text(TestCleanYourBillsActions._PLEDGE_0),
            "Within the next two months, I pledge to switch from my current energy supplier – which is a great green tariff – to a green energy supplier. 2 people live in our home. My house is mainly heated by gas or oil.",
        )
        self.assertEqual(
            TestCleanYourBillsActions._ACTION.get_text(TestCleanYourBillsActions._PLEDGE_1),
            "Within the next two months, I pledge to switch from my current energy supplier – which is bog standard – to a green energy supplier. 2 people live in our home. My house is mainly heated by gas or oil.",
        )
        self.assertEqual(
            TestCleanYourBillsActions._ACTION.get_text(TestCleanYourBillsActions._PLEDGE_2),
            "Within the next two months, I pledge to switch from my current energy supplier – which is a great green tariff – to a green energy supplier. 2 people live in our home. My house is mainly heated by electricity.",
        )
        self.assertEqual(
            TestCleanYourBillsActions._ACTION.get_text(TestCleanYourBillsActions._PLEDGE_3),
            "Within the next two months, I pledge to switch from my current energy supplier – which is bog standard – to a green energy supplier. 2 people live in our home. My house is mainly heated by electricity.",
        )

    def test_invalid_version(self):
        action = actions_models.CleanYourBillsActions(version=-1)
        _Utils.test_invalid_version(self, action)
