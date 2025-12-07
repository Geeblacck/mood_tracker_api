from rest_framework import serializers
from .models import MoodEntry

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ['id', 'user', 'date', 'mood', 'note', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
