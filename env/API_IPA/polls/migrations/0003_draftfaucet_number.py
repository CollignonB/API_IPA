# Generated by Django 4.2.6 on 2023-10-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_beer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftfaucet',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
