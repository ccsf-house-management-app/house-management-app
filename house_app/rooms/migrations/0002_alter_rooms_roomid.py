# Generated by Django 4.0.3 on 2022-03-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='roomId',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
