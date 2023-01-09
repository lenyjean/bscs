# Generated by Django 4.1.2 on 2022-12-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=255)),
                ('your_email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
    ]
