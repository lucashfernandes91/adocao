# Generated by Django 3.0.4 on 2020-03-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['nome'], 'verbose_name': 'pet', 'verbose_name_plural': 'pets'},
        ),
        migrations.AddField(
            model_name='pet',
            name='foto',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]