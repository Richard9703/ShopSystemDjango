# Generated by Django 3.2.13 on 2022-07-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0013_auto_20220710_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
