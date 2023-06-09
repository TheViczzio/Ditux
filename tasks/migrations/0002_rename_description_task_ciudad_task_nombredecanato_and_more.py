# Generated by Django 4.2 on 2023-05-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='ciudad',
        ),
        migrations.AddField(
            model_name='task',
            name='nombreDecanato',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='parroquia',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
