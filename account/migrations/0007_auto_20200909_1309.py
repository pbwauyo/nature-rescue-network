# Generated by Django 3.1 on 2020-09-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/users/profile_images', verbose_name='profile image'),
        ),
    ]
