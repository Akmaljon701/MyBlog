# Generated by Django 4.2.1 on 2023-05-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yutuq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=100)),
                ('sana', models.DateField(auto_now_add=True)),
                ('matn', models.TextField()),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
    ]
