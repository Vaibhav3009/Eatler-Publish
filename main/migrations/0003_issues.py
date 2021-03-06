# Generated by Django 3.0.6 on 2020-06-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200610_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('subject', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=20)),
                ('file', models.FileField(blank=True, upload_to='Issues')),
                ('status', models.CharField(choices=[('Resolved', 'resolved'), ('Unresolved', 'unresolved')], default='Unresolved', max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
