# Generated by Django 4.2 on 2023-11-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_apimodels_delete_apimodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimodels',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
