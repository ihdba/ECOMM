# Generated by Django 5.0.7 on 2024-07-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=255)),
                ('channel_rating', models.CharField(max_length=5)),
                ('channel_description', models.TextField()),
                ('channel_img', models.ImageField(default=None, upload_to='img/foodies/')),
            ],
            options={
                'verbose_name_plural': 'Food Channels',
                'ordering': ['channel_name'],
            },
        ),
    ]
