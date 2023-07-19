# Generated by Django 3.2 on 2023-05-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_firstteam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstteam',
            options={'ordering': ['-pk'], 'verbose_name': 'First Team', 'verbose_name_plural': 'First Team'},
        ),
        migrations.AddField(
            model_name='firstteam',
            name='player_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='firstteam',
            name='player_jersey',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]