# Generated by Django 2.0.5 on 2018-06-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='start_date',
        ),
        migrations.AddField(
            model_name='trip',
            name='start_date_tx',
            field=models.IntegerField(default=0),
        ),
    ]