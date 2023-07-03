"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for generating an image
    path('generation/', views.generation, name='generation'),
    # Page that displays the generated images
    path('gallery/', views.gallery, name='gallery'),
    # Page that displays the user image generation history
    path('user_history/', views.user_history, name='user_history'),
    # Page to show the about us content
    path('about/', views.about, name='about'),
]