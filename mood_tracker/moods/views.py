# moods/views.py

from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFromToRangeFilter
from .models import MoodEntry
from .serializers import MoodEntrySerializer


# Pagination class
class MoodEntryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


# Filter class for MoodEntry
class MoodEntryFilter(FilterSet):
    date = DateFromToRangeFilter()  # allows ?date_after=YYYY-MM-DD&date_before=YYYY-MM-DD

    class Meta:
        model = MoodEntry
        fields = ['mood', 'date']


# List & Create Mood Entries
class MoodEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MoodEntryPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = MoodEntryFilter
    search_fields = ['note']            # Search inside note
    ordering_fields = ['date', 'created_at']

    def get_queryset(self):
        # Only show moods of the logged-in user, newest first
        return MoodEntry.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        # Automatically attach the logged-in user to the new mood entry
        serializer.save(user=self.request.user)


# Retrieve, Update, Delete Mood Entry
class MoodEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow logged-in user to access their own entries
        return MoodEntry.objects.filter(user=self.request.user)
