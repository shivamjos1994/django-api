# Generated by Django 4.2 on 2023-11-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='ApiModel',
        ),
    ]
