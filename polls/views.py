from curses import use_default_colors
import json
from re import S
from telnetlib import STATUS
from django.urls import re_path, reverse_lazy
from django.views import View
from django.views.generic import TemplateView
import requests
from django.shortcuts import redirect, render
from django.http import JsonResponse
from localStoragePy import localStoragePy
from .models import PollSets


class HomePageView(TemplateView):
  template_name = 'home.htm'

class AboutPageView(TemplateView):
  template_name = 'about.htm'

def FoodPollView(request):

  # res = requests.get('http://www.themealdb.com/api/json/v1/1/random.php').json()
  # food_data = PollSets(
  #   item_name = res['meals'][0]['strMeal'], 
  #   item_img = res['meals'][0]['strMealThumb'], 
  #   item_cat = 'food'
  #   )

  # food_data.save()
  foods = PollSets.objects.filter(item_cat='food')

  return render(request, 'food-poll.htm', {'foods': foods})

def MoviesPollView(request):


  # res = requests.get('https://api.themoviedb.org/3/search/movie?api_key=e82e2c2f233a83f1f733511c857285b8&query=action&page=1').json()

  # for data in res['results']:
  #   movie_data = PollSets(
  #     item_name = data['original_title'],
  #     item_img = 'https://image.tmdb.org/t/p/w500'+data['poster_path'],
  #     item_cat = 'movie'
  #     )
  #   movie_data.save()

  movies = PollSets.objects.filter(item_cat='movie')

  return render(request, 'movies-poll.htm', {'movies': movies})

def GamesPollView(request):


  # res = requests.get('https://api.rawg.io/api/games?key=193932b9cb604e338d6fe2b7d9204365&page_size=20').json()

  # for data in res['results']:
  #   game_data = PollSets(
  #     item_name = data['name'],
  #     item_img = data['background_image'],
  #     item_cat = 'game'
  #   )
  #   game_data.save()

  games = PollSets.objects.filter(item_cat='game')

  return render(request, 'games-poll.htm', {'games': games})


class ResultsPageView(View):

  user_picks = []
  top_votes = []

  def post(self,request):
    if (request.method == 'POST'):  

      picks = request.POST.getlist('picks[]')

      for pick in picks:
        vote = PollSets.objects.get(id=pick)
        self.user_picks.append(vote)
        vote.votes +=1
        vote.save()

      top_votes_set = PollSets.objects.filter(item_cat=self.user_picks[0].item_cat)
      top_3_votes = top_votes_set.order_by('-votes')[:3]
      
      for obj in top_3_votes:
        self.top_votes.append(obj)

      return (JsonResponse({}, status=200))
  

  def get(self, request):
    if (request.method == 'GET'):
      return render(request, 'results.htm', context = {'top_votes': self.top_votes, 'user_picks': self.user_picks})


