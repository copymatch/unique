# Generated by Django 5.1.1 on 2024-09-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copywriter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('work', models.CharField(max_length=1000)),
            ],
        ),
    ]
