# Generated by Django 5.1.5 on 2025-01-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.IntegerField(max_length=12)),
            ],
        ),
    ]
