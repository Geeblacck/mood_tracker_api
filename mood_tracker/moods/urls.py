from django.urls import path
from .views import MoodEntryListCreateView, MoodEntryDetailView

urlpatterns = [
    path('moods/', MoodEntryListCreateView.as_view(), name='mood-list-create'),
    path('moods/<int:pk>/', MoodEntryDetailView.as_view(), name='mood-detail'),
]
