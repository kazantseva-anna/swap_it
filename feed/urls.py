from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
]