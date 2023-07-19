"""
URL configuration for wallpassFC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news import views as news_views

app_name = 'news'

urlpatterns = [
    path('announcements', news_views.AnnouncementView.as_view(), name="Announcement Data"),
    path('announcements/<int:pk>', news_views.AnnouncementDetailedView.as_view(), name="Announcement Data"),
    path('clubData', news_views.ClubDataView.as_view(), name="ClubDetails"),
    path('trophy', news_views.TrophyView.as_view(), name="Trophy"),
    path('video', news_views.VideoView.as_view(), name="Video"),
    path('owner', news_views.OwnerImageView.as_view(), name="Owner"),
    path('team', news_views.FirstTeamView.as_view(), name="team"),
    path('student',news_views.ClubStudentDetailedView.as_view(),name='student')
]
