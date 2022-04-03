# Generated by Django 4.0.3 on 2022-04-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='date_due',
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]