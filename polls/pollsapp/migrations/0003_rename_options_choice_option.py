# Generated by Django 4.0.1 on 2023-02-16 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0002_rename_question_text_question_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='options',
            new_name='option',
        ),
    ]
