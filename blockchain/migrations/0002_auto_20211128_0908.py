# Generated by Django 3.2.9 on 2021-11-28 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='l3btcusdasks',
            options={'verbose_name': 'L3BT-USD Ask', 'verbose_name_plural': 'L3BT-USD Asks'},
        ),
        migrations.AlterModelOptions(
            name='l3btcusdbids',
            options={'verbose_name': 'L3BT-USD Bid', 'verbose_name_plural': 'L3BT-USD Bids'},
        ),
    ]