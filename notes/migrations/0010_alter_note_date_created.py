# Generated by Django 5.1 on 2024-09-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_note_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]