from django.urls import path, include
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('post/new/', BlogCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='contact')
]
