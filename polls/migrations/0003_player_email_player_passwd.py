# Generated by Django 4.0.4 on 2022-05-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='passwd',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
