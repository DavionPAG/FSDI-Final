from django.urls import path
from .views import HomePageView, AboutPageView, PollPageView, ResultsPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about_devs', AboutPageView.as_view(), name='about'),
  path('poll', PollPageView.as_view(), name='poll'),
  path('results', ResultsPageView.as_view(), name='results'),
]