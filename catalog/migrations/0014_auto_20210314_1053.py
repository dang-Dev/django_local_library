# Generated by Django 3.1.7 on 2021-03-14 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20210312_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tmodel',
            old_name='search',
            new_name='search_book',
        ),
        migrations.CreateModel(
            name='TModelAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.tmodelauthor')),
            ],
        ),
    ]
