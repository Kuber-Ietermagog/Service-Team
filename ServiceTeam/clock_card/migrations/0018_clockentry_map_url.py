# Generated by Django 2.0.2 on 2019-04-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock_card', '0017_auto_20190429_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='clockentry',
            name='map_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]