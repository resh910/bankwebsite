# Generated by Django 4.1.3 on 2023-02-08 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='mailid',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='name',
            new_name='first_name',
        ),
    ]
