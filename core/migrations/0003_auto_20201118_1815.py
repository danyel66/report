# Generated by Django 3.0 on 2020-11-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201118_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suicidestat',
            name='suicides_no',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
