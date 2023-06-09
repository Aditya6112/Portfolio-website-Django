# Generated by Django 4.2.1 on 2023-06-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=7)),
                ('concern', models.TextField()),
            ],
        ),
    ]
