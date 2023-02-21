from django.urls import path
from apps.settings.views import index, privacy, about,contacts
urlpatterns = [
    path('', index, name='index'),
    path('privacy/', privacy, name = 'privacy'),
    path('about/', about, name = 'about'),
    path('contacts/', contacts, name='contacts'),
]

