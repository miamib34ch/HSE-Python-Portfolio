from django.views.generic import DetailView, ListView
from jobs.models import Job


class IndexJobsListView(ListView):
    model = Job


class IndexJobDetailView(DetailView):
    model = Job
