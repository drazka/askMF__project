# Generated by Django 2.0.4 on 2018-04-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NIP_checker_app', '0005_auto_20180422_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nip',
            name='nip_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
