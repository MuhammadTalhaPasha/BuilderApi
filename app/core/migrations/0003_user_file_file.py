# Generated by Django 2.1.15 on 2020-03-08 08:55

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_file',
            name='file',
            field=models.FileField(null=True, upload_to=core.models.userfile_file_path),
        ),
    ]
