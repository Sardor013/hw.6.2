# Generated by Django 5.0.6 on 2024-05-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]