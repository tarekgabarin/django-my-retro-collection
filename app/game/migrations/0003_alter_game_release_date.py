# Generated by Django 3.2.18 on 2023-04-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20230406_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
