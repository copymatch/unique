# Generated by Django 5.1.3 on 2024-11-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_message_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='unread',
            field=models.BooleanField(null=True),
        ),
    ]