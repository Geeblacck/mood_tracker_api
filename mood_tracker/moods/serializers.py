# moods/serializers.py

from rest_framework import serializers
from .models import MoodEntry
from django.utils import timezone

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ['id', 'user', 'date', 'mood', 'note', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate_date(self, value):
        """
        Ensure that the mood entry date is not in the future.
        """
        if value > timezone.now().date():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value

    def validate(self, attrs):
        """
        Ensure that each user has only one mood entry per day.
        """
        user = self.context['request'].user
        date_value = attrs.get('date')

        # Check for existing entry for the same user and date
        if MoodEntry.objects.filter(user=user, date=date_value).exists():
            raise serializers.ValidationError({
                "non_field_errors": ["You already have a mood entry for this date."]
            })
        return attrs

    def create(self, validated_data):
        """
        Assign the authenticated user automatically on creation.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
