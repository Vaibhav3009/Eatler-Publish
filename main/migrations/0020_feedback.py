# Generated by Django 3.0.6 on 2020-06-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200615_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=2000)),
                ('feedback_type', models.CharField(max_length=30)),
            ],
        ),
    ]
