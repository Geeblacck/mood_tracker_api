# mood_tracker/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # if you have accounts app
    path('api/moods/', include('moods.urls')),       # moods API
    path('api-auth/', include('rest_framework.urls')), # DRF login/logout
    path('', RedirectView.as_view(url='/api/moods/', permanent=False)), # redirect root
]
