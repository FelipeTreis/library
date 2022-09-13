# Generated by Django 4.1.1 on 2022-09-13 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PublishingCompany",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=255)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("New", "New"),
                            ("Semi new", "Semi new"),
                            ("Used", "Used"),
                        ],
                        max_length=15,
                    ),
                ),
                ("is_available", models.BooleanField(default=False)),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                ("category", models.ManyToManyField(to="app.category")),
                (
                    "publishing_company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.publishingcompany",
                    ),
                ),
            ],
        ),
    ]