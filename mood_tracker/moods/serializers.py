from rest_framework import serializers
from .models import MoodEntry

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ['id', 'user', 'date', 'mood', 'note', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


from rest_framework import serializers
from .models import MoodEntry
from django.utils import timezone

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ['id', 'user', 'date', 'mood', 'note', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

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
        date = attrs.get('date')

        if MoodEntry.objects.filter(user=user, date=date).exists():
            raise serializers.ValidationError("You already have a mood entry for this date.")
        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
