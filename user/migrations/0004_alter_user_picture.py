# Generated by Django 4.2 on 2023-04-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/2023-04-16 22:06:39.046431'),
        ),
    ]
