# Generated by Django 3.2.8 on 2021-10-19 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexx', '0002_auto_20211018_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='indexx.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='apelido',
            field=models.CharField(max_length=20, null=True),
        ),
    ]