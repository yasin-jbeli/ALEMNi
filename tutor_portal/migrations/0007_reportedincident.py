# Generated by Django 4.2.7 on 2023-12-06 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tutor_portal", "0006_user_is_banned"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportedIncident",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("resolved", models.BooleanField(default=False)),
                (
                    "reported_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reported_user",
                        to="tutor_portal.user",
                    ),
                ),
                (
                    "reporter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tutor_portal.user",
                    ),
                ),
            ],
        ),
    ]