# Generated by Django 2.2.16 on 2022-06-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220621_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
