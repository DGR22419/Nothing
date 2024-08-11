# Generated by Django 5.0.8 on 2024-08-08 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=55, null=True, unique=True)),
                ('profile_img', models.ImageField(blank=True, default='user.png', null=True, upload_to='profile_images')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
