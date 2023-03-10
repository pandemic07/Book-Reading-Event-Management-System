# Generated by Django 3.2.17 on 2023-03-09 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_event_organiser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organiser', to='api.user'),
        ),
        migrations.AlterField(
            model_name='event',
            name='users_invited',
            field=models.ManyToManyField(blank=True, related_name='users_invited', to='api.User'),
        ),
    ]