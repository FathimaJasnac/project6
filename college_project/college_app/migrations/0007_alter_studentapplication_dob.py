# Generated by Django 4.2.6 on 2024-01-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0006_alter_studentapplication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplication',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
