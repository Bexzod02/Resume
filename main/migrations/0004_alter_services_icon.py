# Generated by Django 3.2.13 on 2022-07-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_services_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.CharField(max_length=50),
        ),
    ]
