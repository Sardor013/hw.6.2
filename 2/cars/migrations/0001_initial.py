# Generated by Django 5.0.6 on 2024-05-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=225)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
