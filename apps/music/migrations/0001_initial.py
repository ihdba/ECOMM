# Generated by Django 5.0.7 on 2024-07-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=255)),
                ('m_description', models.TextField()),
                ('m_img', models.ImageField(blank=True, default=None, null=True, upload_to='img/foodies/')),
                ('m_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Music',
                'ordering': ['m_name'],
            },
        ),
    ]