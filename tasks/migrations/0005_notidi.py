# Generated by Django 4.2 on 2023-05-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_parro_horasanta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notidi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('noticia', models.TextField(blank=True)),
            ],
        ),
    ]
