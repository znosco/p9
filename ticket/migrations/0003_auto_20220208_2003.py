# Generated by Django 3.1.4 on 2022-02-08 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20220208_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
