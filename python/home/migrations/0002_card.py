# Generated by Django 4.2.4 on 2023-10-31 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('stk', models.IntegerField(default=0)),
                ('sd', models.IntegerField(default=0)),
                ('banlk', models.CharField(max_length=50)),
            ],
        ),
    ]
