# Generated by Django 5.0.6 on 2024-05-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.IntegerField()),
                ('price', models.IntegerField()),
                ('village', models.CharField(max_length=225)),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]
