# Generated by Django 3.2.13 on 2022-04-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_resume_is_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='type',
            field=models.IntegerField(choices=[('Education', 'Education'), ('Experience', 'Experience'), ('Skills', 'Skills'), ('Awards', 'Awards')]),
        ),
    ]