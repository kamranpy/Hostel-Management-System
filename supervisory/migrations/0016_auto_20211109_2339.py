# Generated by Django 3.2.9 on 2021-11-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisory', '0015_auto_20211108_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='roomCapacity',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='roomFee',
        ),
        migrations.AlterField(
            model_name='hostelapply',
            name='ac',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hostelapply',
            name='mess',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hostelapply',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
