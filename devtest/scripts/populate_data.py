import actions.models as actions_models
import pledges.models as pledges_models

from django.contrib.auth.models import User


def run():
    action_type_veg_out = actions_models.ActionType(name="Veg Out")
    action_type_veg_out.save()
    action_type_clean_your_bills = actions_models.ActionType(name="Clean your Bills")
    action_type_clean_your_bills.save()

    action_veg_out_ver_0 = actions_models.VegOutAction(
        version=0,
        action_type=action_type_veg_out,
    )
    action_veg_out_ver_0.save()

    action_clean_your_bills_ver_0 = actions_models.CleanYourBillsActions(
        version=0,
        action_type=action_type_clean_your_bills,
    )
    action_clean_your_bills_ver_0.save()

    # region User 0
    user_0 = User.objects.create_user("user_0", "user_0@example.com", "user_0")

    pledge_veg_out_0 = pledges_models.VegOutPledge(
        user=user_0,
        current_meals=1,
        veggie_meals=pledges_models.VegOutVeggieMeals.ZERO_TO_FIVE,
        action=action_veg_out_ver_0,
    )
    pledge_veg_out_0.save()

    pledge_clean_your_bills_0 = pledges_models.CleanYourBillsPledge(
        user=user_0,
        energy_supplier=pledges_models.CleanYourBillsEnergySupplier.STANDARD,
        number_of_people=2,
        heating_source=pledges_models.CleanYourBillsHeatingSource.GAS_OR_OIL,
        action=action_clean_your_bills_ver_0,
    )
    pledge_clean_your_bills_0.save()
    # endregion

    # region User 1
    user_1 = User.objects.create_user("user_1", "user_1@example.com", "user_1")

    pledge_veg_out_1 = pledges_models.VegOutPledge(
        user=user_1,
        current_meals=5,
        veggie_meals=pledges_models.VegOutVeggieMeals.SIX_PLUS,
        action=action_veg_out_ver_0,
    )
    pledge_veg_out_1.save()
    # endregion

    # region User 2
    user_2 = User.objects.create_user("user_2", "user_2@example.com", "user_2")

    pledge_clean_your_bills_1 = pledges_models.CleanYourBillsPledge(
        user=user_2,
        energy_supplier=pledges_models.CleanYourBillsEnergySupplier.GREEN,
        number_of_people=7,
        heating_source=pledges_models.CleanYourBillsHeatingSource.ELECTRICITY,
        action=action_clean_your_bills_ver_0,
    )
    pledge_clean_your_bills_1.save()
    # endregion


if __name__ == "__main__":
    run()
