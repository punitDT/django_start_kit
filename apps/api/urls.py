from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='api_login'),
]