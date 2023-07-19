from django.shortcuts import render
from rest_framework import generics
from .models import Announcement, Club, Trophy, Video, Staff, FirstTeam, ClubStudent
from .serializers import AnnouncementSerializer, AnnouncementDetailSerializer, ClubDataSerializer, TrophySerializer, \
    VideoSerializer, OwnerSerializer, FirstTeamSerializer, ClubStudentSerializer,PracticePostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend


class AnnouncementView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["news_type"]


class AnnouncementDetailedView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer


class ClubDataView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubDataSerializer


class TrophyView(ListAPIView):
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer


class VideoView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class OwnerImageView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = OwnerSerializer


class FirstTeamView(ListAPIView):
    queryset = FirstTeam.objects.all()
    serializer_class = FirstTeamSerializer


class ClubStudentDetailedView(ListAPIView):
    queryset = ClubStudent.objects.all()
    serializer_class = ClubStudentSerializer

