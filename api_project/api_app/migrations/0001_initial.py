# Generated by Django 3.2.21 on 2023-09-14 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Name can only contain letters and spaces.', regex='^[a-zA-Z\\s]+$')])),
            ],
        ),
    ]
