# Generated by Django 3.2.8 on 2021-10-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexx', '0003_auto_20211018_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nascimento',
            field=models.DateField(),
        ),
    ]