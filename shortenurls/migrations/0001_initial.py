# Generated by Django 4.0.4 on 2022-05-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourURL', models.CharField(max_length=100)),
                ('shortURL', models.CharField(max_length=50)),
            ],
        ),
    ]
