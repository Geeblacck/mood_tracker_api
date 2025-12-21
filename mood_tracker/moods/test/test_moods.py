# moods/test/test_moods.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from moods.models import MoodEntry


class MoodEntryTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="strongpassword123"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_mood_entry(self):
        url = reverse('mood-list')
        data = {
            "mood": "happy",
            "date": date.today()  # <-- changed from entry_date
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MoodEntry.objects.count(), 1)
        self.assertEqual(MoodEntry.objects.first().mood, "happy")

    def test_duplicate_mood_same_day_fails(self):
        url = reverse('mood-list')
        data = {
            "mood": "happy",
            "date": date.today()
        }

        self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_future_date_not_allowed(self):
        url = reverse('mood-list')
        data = {
            "mood": "sad",
            "date": date.today() + timedelta(days=1)
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('date', response.data)

    def test_filter_by_mood(self):
        url = reverse('mood-list')

        self.client.post(url, {"mood": "happy", "date": date.today()}, format='json')
        self.client.post(url, {"mood": "sad", "date": date.today() - timedelta(days=1)}, format='json')

        response = self.client.get(url + "?mood=happy")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['mood'], 'happy')

    def test_pagination_works(self):
        url = reverse('mood-list')

        # Create 15 entries to test pagination (default page_size=10)
        for i in range(15):
            self.client.post(url, {
                "mood": f"neutral{i}",
                "date": date.today() - timedelta(days=i)
            }, format='json')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 10)  # page_size
        self.assertIn('next', response.data)
        self.assertIsNotNone(response.data['next'])
