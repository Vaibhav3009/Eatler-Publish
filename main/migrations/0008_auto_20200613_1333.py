# Generated by Django 3.0.6 on 2020-06-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200612_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='schedule_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='schedule_time',
            field=models.TimeField(default=None),
        ),
    ]
