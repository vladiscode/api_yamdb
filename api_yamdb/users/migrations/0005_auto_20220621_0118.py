# Generated by Django 2.2.16 on 2022-06-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220621_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.IntegerField(),
        ),
    ]
