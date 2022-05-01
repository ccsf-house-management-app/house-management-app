# Generated by Django 4.0.3 on 2022-05-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_alter_roomsassign_remarks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='rent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='roomDescription',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='roomName',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
