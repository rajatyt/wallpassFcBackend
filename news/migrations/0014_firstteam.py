# Generated by Django 3.2 on 2023-05-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20230526_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
