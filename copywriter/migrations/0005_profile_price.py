# Generated by Django 5.1.1 on 2024-10-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copywriter', '0004_profile_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
