# Generated by Django 3.2.6 on 2021-08-28 04:06

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementCenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeraccount',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeraccount',
            name='birth_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeraccount',
            name='current_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeraccount',
            name='national_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeraccount',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
