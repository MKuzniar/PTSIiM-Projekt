# Generated by Django 3.2.8 on 2021-11-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]