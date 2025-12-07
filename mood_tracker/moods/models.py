from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    # Link each mood entry to its user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_entries')
    
    # Date of the mood log
    date = models.DateField()
    
    # Mood choice
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
        ('anxious', 'Anxious'),
        ('excited', 'Excited'),
    ]
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    
    # Optional note
    note = models.TextField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'date')  # ensures one mood entry per user per day
        ordering = ['-date']  # newest first
    
    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.mood}"
