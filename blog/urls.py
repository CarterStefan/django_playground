from django.urls import path
from .views import BlogListView, BlogDetailedView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailedView.as_view(), name='post-detail'),
]
