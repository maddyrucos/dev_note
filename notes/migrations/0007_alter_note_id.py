# Generated by Django 5.1 on 2024-09-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_note_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
