# Generated by Django 2.0.2 on 2019-04-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock_card', '0005_auto_20190408_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockentry',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
