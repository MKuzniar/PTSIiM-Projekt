# Generated by Django 3.2.8 on 2021-11-20 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_api', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='clinic_api.doctor'),
        ),
    ]
