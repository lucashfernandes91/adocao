# Generated by Django 3.0.4 on 2020-03-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('responsavel', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=50)),
            ],
        ),
    ]
