# Generated by Django 4.1.2 on 2022-12-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
