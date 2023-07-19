from django.db import models
from news.constant import STAFF_TYPE, TEAM, NEWS, CATEGORY


# Create your models here.
class Announcement(models.Model):
    news_type = models.CharField(choices=NEWS, default="Overall", max_length=255)
    newsImage = models.ImageField(upload_to="images", null=True, blank=True)
    newsShortDesc = models.CharField(max_length=255, null=True)
    uploadDate = models.DateTimeField(auto_now=True)
    newsDescription = models.CharField(max_length=2555, null=True)
    topScorer = models.CharField(max_length=255, null=True)
    playerOfTheSeason = models.CharField(max_length=255, null=True)
    goalOfTheSeason = models.CharField(max_length=255, null=True)
    emergingPlayer = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
        ordering = ["-pk"]


class Club(models.Model):
    # about = models.CharField(max_length=2555)
    # motto = models.CharField(max_length=2555)
    gallery = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta:
        ordering = ["-pk"]


class Trophy(models.Model):
    trophyName = models.CharField(max_length=255)
    trophyYear = models.CharField(max_length=255)
    trophyImage = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta:
        ordering = ["-pk"]


class Video(models.Model):
    viewData = models.FileField(upload_to="video", null=True, blank=True)
    videoYoutube = models.CharField(max_length=255)

    class Meta:
        ordering = ["-pk"]


class Staff(models.Model):
    ownerImage = models.ImageField(upload_to="images", null=True, blank=True)
    ownerName = models.CharField(max_length=255, null=True)
    user_type = models.CharField(max_length=100, choices=STAFF_TYPE, default="owner", verbose_name="Staff type",
                                 null=True)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"
        ordering = ["-pk"]


class FirstTeam(models.Model):
    player_choice = models.CharField(choices=TEAM, default="Forwards", max_length=255)
    player_image = models.ImageField(upload_to="images", blank=True, null=True)
    player_name = models.CharField(max_length=255)
    player_jersey = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "First Team"
        verbose_name_plural = "First Team"
        ordering = ["-pk"]


class ClubStudent(models.Model):
    student_image = models.ImageField(upload_to="images", blank=True, null=True)
    student_name = models.CharField(max_length=255)
    student_jersey_no = models.IntegerField(null=True, default=0)
    position = models.CharField(choices=TEAM, null=True, blank=True, max_length=255)
    category = models.CharField(choices=CATEGORY, null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "ClubStudent"
        verbose_name_plural = "Club Students"
        ordering = ["-pk"]


class PracticePost(models.Model):
    name_post = models.CharField(max_length=255)
    image_post = models.ImageField(upload_to="images", null=True, blank=True)
    datetime_post = models.DateTimeField(auto_now=True)
    number_post = models.IntegerField()
