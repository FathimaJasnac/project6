# Generated by Django 4.2.6 on 2024-01-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0008_alter_studentapplication_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplication',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
