# Generated by Django 2.0.2 on 2019-04-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190405_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]