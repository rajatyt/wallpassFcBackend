# Generated by Django 3.2 on 2023-05-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_trophy_trophyimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewData', models.FileField(blank=True, null=True, upload_to='video')),
                ('videoYoutube', models.CharField(max_length=255)),
            ],
        ),
    ]