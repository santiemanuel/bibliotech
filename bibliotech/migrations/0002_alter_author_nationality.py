# Generated by Django 4.2.1 on 2023-05-24 13:02

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("bibliotech", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="nationality",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, null=True
            ),
        ),
    ]
