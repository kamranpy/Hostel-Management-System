# Generated by Django 3.2.9 on 2021-11-07 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervisory', '0011_mess'),
    ]

    operations = [
        migrations.AddField(
            model_name='mess',
            name='rHostelName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisory.hostel'),
        ),
    ]
