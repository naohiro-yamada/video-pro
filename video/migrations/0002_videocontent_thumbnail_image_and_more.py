# Generated by Django 4.2.1 on 2023-06-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocontent',
            name='thumbnail_image',
            field=models.FileField(default='', upload_to='thumbnail'),
        ),
        migrations.AlterField(
            model_name='videocontent',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
