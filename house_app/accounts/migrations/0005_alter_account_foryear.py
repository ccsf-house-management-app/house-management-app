# Generated by Django 4.0.3 on 2022-04-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_foryear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='foryear',
            field=models.IntegerField(blank=True, choices=[('2022', '2022'), ('2023', '2023'), ('2024', '2024')], null=True),
        ),
    ]
