# Generated by Django 2.2.1 on 2019-06-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0002_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='umpire3',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
