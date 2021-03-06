# Generated by Django 3.2.9 on 2021-11-04 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervisory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('app_status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Denied', 'Denied')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisory.customer')),
                ('hostel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisory.hostel')),
            ],
        ),
    ]
