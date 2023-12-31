# Generated by Django 3.2 on 2023-05-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_category_announcement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-pk'], 'verbose_name': 'Announcement', 'verbose_name_plural': 'Announcements'},
        ),
        migrations.AddField(
            model_name='announcement',
            name='emergingPlayer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='goalOfTheSeason',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='newsDescription',
            field=models.CharField(max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='playerOfTheSeason',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='topScorer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='newsShortDesc',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
