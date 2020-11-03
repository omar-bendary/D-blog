from django.urls import path
from .views import HomePostsView

urlpatterns = [
    path('', HomePostsView.as_view(), name='home')
]
