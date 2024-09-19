from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
]
