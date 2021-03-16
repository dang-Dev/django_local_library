# Generated by Django 3.1.7 on 2021-03-16 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20210316_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='TModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_author_models', to='catalog.tmodel')),
                ('book_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_book_models', to='catalog.tmodel')),
            ],
        ),
        migrations.RemoveField(
            model_name='tmodelbook',
            name='book',
        ),
        migrations.DeleteModel(
            name='TModelAuthor',
        ),
        migrations.DeleteModel(
            name='TModelBook',
        ),
    ]
