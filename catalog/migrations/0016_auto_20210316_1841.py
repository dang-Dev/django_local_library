# Generated by Django 3.1.7 on 2021-03-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_delete_tmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TModelAuthor',
            new_name='TModel',
        ),
    ]
