# Generated by Django 3.0.3 on 2022-01-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20211119_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofilemodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='driverreviewmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
