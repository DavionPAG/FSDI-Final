from django.urls import path
from .views import HomePageView, AboutPageView, ResultsPageView
from . import views

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about_devs/', AboutPageView.as_view(), name='about'),
  path('food-poll/', views.FoodPollView, name='food-poll'),
  path('movies-poll/', views.MoviesPollView, name='movies-poll'),
  path('games-poll/', views.GamesPollView, name='games-poll'),
  path('results/', ResultsPageView.as_view(), name='results'),
]