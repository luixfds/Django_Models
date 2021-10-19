# Generated by Django 3.2.8 on 2021-10-19 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'produtin',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='apelido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data do Registro'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nome de Usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='senha',
            field=models.CharField(max_length=10),
        ),
    ]
