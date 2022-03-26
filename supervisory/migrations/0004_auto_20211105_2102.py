# Generated by Django 3.2.9 on 2021-11-05 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervisory', '0003_hostelapply_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelapply',
            name='rooms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisory.rooms'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='roomStatus',
            field=models.CharField(choices=[('Vacant', 'Vacant'), ('Occupied', 'Occupied')], max_length=200, null=True),
        ),
    ]
