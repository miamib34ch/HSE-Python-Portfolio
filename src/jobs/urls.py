from django.urls import path
from jobs.views import IndexJobsListView, IndexJobDetailView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name='jobs'),
    path("<int:pk>/", IndexJobDetailView.as_view(), name='job')
]