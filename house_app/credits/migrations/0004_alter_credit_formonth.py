# Generated by Django 4.0.3 on 2022-03-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0003_credit_foryear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='formonth',
            field=models.IntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], max_length=2, null=True),
        ),
    ]
