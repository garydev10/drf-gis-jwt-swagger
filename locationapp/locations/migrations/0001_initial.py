# Generated by Django 4.1.2 on 2022-10-23 05:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=100)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
