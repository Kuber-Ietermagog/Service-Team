# Generated by Django 2.0.2 on 2019-04-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock_card', '0003_auto_20190408_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockentry',
            name='date',
            field=models.DateTimeField(),
        ),
    ]