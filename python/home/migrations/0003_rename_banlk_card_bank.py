# Generated by Django 4.2.4 on 2023-10-31 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='banlk',
            new_name='bank',
        ),
    ]
