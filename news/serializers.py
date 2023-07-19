from rest_framework import serializers
from .models import Announcement, Club, Trophy, Video, Staff, FirstTeam, ClubStudent, PracticePost


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            "id", "newsImage", "newsShortDesc", "uploadDate", "news_type"
        ]


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"


class ClubDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["gallery"]


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["viewData", "videoYoutube"]


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class FirstTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstTeam
        fields = "__all__"


class ClubStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubStudent
        fields = "__all__"


class PracticePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticePost
        field = "__all__"
