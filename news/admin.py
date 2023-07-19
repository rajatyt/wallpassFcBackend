from django.contrib import admin
from .models import Announcement, Club, Trophy, Video, Staff, FirstTeam, ClubStudent


# Register your models here.
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["id", "news_type", "newsImage", "newsShortDesc", "uploadDate", "newsDescription", "topScorer",
                    "playerOfTheSeason", "goalOfTheSeason", "emergingPlayer"]


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["gallery"]


@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ["trophyName", "trophyYear", "trophyImage"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["viewData", "videoYoutube"]


@admin.register(Staff)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["ownerImage", "ownerName", "user_type"]


@admin.register(FirstTeam)
class FirstTeamAdmin(admin.ModelAdmin):
    list_display = ["player_choice", "player_image", "player_name", "player_jersey"]

@admin.register(ClubStudent)
class ClubStudent(admin.ModelAdmin):
    list_display = ["category","position","student_jersey_no","student_name","student_image"]
