# Generated by Django 3.1.4 on 2022-10-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pertsona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('izena', models.CharField(max_length=255)),
                ('abizena', models.CharField(max_length=255)),
                ('jaiotzeData', models.DateTimeField()),
            ],
        ),
    ]
