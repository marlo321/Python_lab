# Generated by Django 2.1.2 on 2018-11-09 11:57

import django.contrib.auth.models
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181101_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='participants',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', ''), ('Alex', 'Alex'), ('Andrey', 'Andrey'), ('Helen', 'Helen'), ('Nick', 'Nick'), ('admin', 'admin')], default=django.contrib.auth.models.User, max_length=100),
        ),
    ]