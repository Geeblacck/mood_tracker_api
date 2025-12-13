from rest_framework import generics, permissions
from .models import MoodEntry
from .serializers import MoodEntrySerializer

# List and Create Mood Entries
class MoodEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return mood entries for the logged-in user
        return MoodEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the owner
        serializer.save(user=self.request.user)

# Retrieve, Update, Delete Mood Entry
class MoodEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)
#end


from rest_framework import generics, permissions
from .models import MoodEntry
from .serializers import MoodEntrySerializer

class MoodEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


# moods/views.py
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import MoodEntry
from .serializers import MoodEntrySerializer

# Pagination class
class MoodEntryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

# List and create moods with filtering and pagination
class MoodEntryListCreateView(generics.ListCreateAPIView):
    queryset = MoodEntry.objects.all().order_by('-date')
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MoodEntryPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['date', 'mood', 'user']  # filtering options
    search_fields = ['note']  # search in notes
    ordering_fields = ['date', 'created_at']  # ordering options
