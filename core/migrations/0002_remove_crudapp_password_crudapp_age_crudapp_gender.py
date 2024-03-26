# Generated by Django 5.0.3 on 2024-03-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crudapp',
            name='password',
        ),
        migrations.AddField(
            model_name='crudapp',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='crudapp',
            name='gender',
            field=models.CharField(default='male', max_length=25),
        ),
    ]