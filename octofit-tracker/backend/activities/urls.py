from django.urls import path

from .views import ActivityListCreateView

app_name = 'activities'

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
]
