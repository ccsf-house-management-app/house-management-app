# Generated by Django 4.0.3 on 2022-03-30 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crid', models.CharField(blank=True, max_length=25, null=True)),
                ('crname', models.CharField(choices=[('a', 'Chores'), ('b', 'Groceries'), ('c', 'Other')], default='Chores', max_length=10)),
                ('cracccount', models.CharField(blank=True, max_length=25, null=True)),
                ('cramount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_cr', models.DateField()),
                ('date_done', models.DateField()),
                ('crdescription', models.TextField(max_length=200)),
                ('cruserid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
