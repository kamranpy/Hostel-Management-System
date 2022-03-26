# Generated by Django 3.2.9 on 2021-11-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisory', '0008_hostelapply_feestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelapply',
            name='challan_no',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='hostelapply',
            name='upload_challan',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='hostelapply',
            name='feeStatus',
            field=models.CharField(choices=[('Paid', 'Paid'), ('UnPaid', 'UnPaid')], default='UnPaid', max_length=200, null=True),
        ),
    ]