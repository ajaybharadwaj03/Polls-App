# Generated by Django 4.0.1 on 2023-02-16 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]
