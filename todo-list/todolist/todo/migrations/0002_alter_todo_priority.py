# Generated by Django 4.1.6 on 2023-02-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[(None, 'Please Choose'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=20),
        ),
    ]
