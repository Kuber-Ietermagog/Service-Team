# Generated by Django 2.0.2 on 2019-04-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock_card', '0010_auto_20190409_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockentry',
            name='clock_io',
            field=models.CharField(blank=True, choices=[('In', 'In'), ('Out', 'OUT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='clockentry',
            name='work_st',
            field=models.CharField(blank=True, choices=[('Work', 'Work'), ('Travel', 'Travel')], max_length=100),
        ),
    ]