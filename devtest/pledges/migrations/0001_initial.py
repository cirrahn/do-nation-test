# Generated by Django 3.2.4 on 2021-06-26 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("actions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="VegOutPledge",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("current_meals", models.IntegerField()),
                ("veggie_meals", models.CharField(choices=[("05", "0-5"), ("6P", "6+")], max_length=2)),
                ("action", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="actions.vegoutaction")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CleanYourBillsPledge",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "energy_supplier",
                    models.CharField(choices=[("BS", "bog standard"), ("GG", "a great green tariff")], max_length=2),
                ),
                ("number_of_people", models.IntegerField()),
                (
                    "heating_source",
                    models.CharField(choices=[("GO", "gas or oil"), ("EC", "electricity")], max_length=2),
                ),
                (
                    "action",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="actions.cleanyourbillsactions"),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
