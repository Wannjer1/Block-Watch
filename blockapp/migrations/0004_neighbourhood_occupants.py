# Generated by Django 4.0.4 on 2022-06-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockapp', '0003_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='occupants',
            field=models.IntegerField(default=0),
        ),
    ]
