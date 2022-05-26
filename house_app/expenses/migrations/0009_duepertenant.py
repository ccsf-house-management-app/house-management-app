# Generated by Django 4.0.3 on 2022-05-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_delete_monthlydue'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuePerTenant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('formonth', models.IntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True)),
                ('foryear', models.CharField(blank=True, choices=[('2022', '2022'), ('2023', '2023'), ('2024', '2024')], default='2022', max_length=4, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
