# Generated by Django 5.0.2 on 2024-04-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='internet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]