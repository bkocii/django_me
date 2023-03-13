# Generated by Django 4.1.4 on 2023-03-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('EN', 'English Language Course'), ('GER', 'German Language Course')], default='GER', max_length=20),
        ),
    ]
