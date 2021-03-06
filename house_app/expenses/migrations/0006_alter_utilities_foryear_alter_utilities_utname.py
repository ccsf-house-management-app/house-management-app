# Generated by Django 4.0.3 on 2022-04-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_alter_utilities_formonth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilities',
            name='foryear',
            field=models.CharField(blank=True, choices=[('2022', '2022'), ('2023', '2023'), ('2024', '2024')], default='2022', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='utilities',
            name='utname',
            field=models.CharField(choices=[('PGE', 'PGE'), ('Water', 'Water'), ('TvCable', 'TV/Cable'), ('WIFI', 'WIFI'), ('Groceries', 'Groceries'), ('Other', 'Other')], default='PGE', max_length=10),
        ),
    ]
