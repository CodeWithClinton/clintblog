# Generated by Django 3.1 on 2021-07-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/image/fs1.jpg', upload_to='pics'),
        ),
    ]