from django.urls import path
from .views import MoodEntryListCreateView, MoodEntryDetailView

urlpatterns = [
    path('moods/', MoodEntryListCreateView.as_view(), name='mood-list-create'),
    path('moods/<int:pk>/', MoodEntryDetailView.as_view(), name='mood-detail'),
]


# moods/urls.py
from django.urls import path
from .views import MoodEntryListCreateView, MoodEntryRetrieveUpdateDestroyView

urlpatterns = [
    path('moods/', MoodEntryListCreateView.as_view(), name='mood-list-create'),
    path('moods/<int:pk>/', MoodEntryRetrieveUpdateDestroyView.as_view(), name='mood-detail'),
]
