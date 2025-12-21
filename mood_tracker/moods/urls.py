# moods/urls.py
from django.urls import path
from .views import MoodEntryListCreateView, MoodEntryDetailView

urlpatterns = [
    path('', MoodEntryListCreateView.as_view(), name='mood-list'),      # GET / POST moods
    path('<int:pk>/', MoodEntryDetailView.as_view(), name='mood-detail'), # GET / PUT / DELETE a mood
]
