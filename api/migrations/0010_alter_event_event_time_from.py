# Generated by Django 3.2.17 on 2023-03-12 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_event_event_time_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 20, 12, 20, 330009)),
        ),
    ]
