# Generated by Django 3.2 on 2023-05-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20230526_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstteam',
            name='player_choice',
            field=models.CharField(choices=[('Goalkeepers', 'Goalkeepers'), ('Defenders', 'Defenders'), ('Midfielders', 'Midfielders'), ('Forwards', 'Forwards'), ('CoachingStaff', 'CoachingStaff')], default='Forwards', max_length=255),
        ),
    ]
