from django.views.generic import TemplateView
import requests
from django.shortcuts import render
from .models import PollSets

class HomePageView(TemplateView):
  template_name = 'home.htm'

class AboutPageView(TemplateView):
  template_name = 'about.htm'

def FoodPollView(request):
  res = requests.get('http://www.themealdb.com/api/json/v1/1/random.php').json()
  food_data = PollSets(
    item_name = res['meals'][0]['strMeal'], 
    item_img = res['meals'][0]['strMealThumb'], 
    item_cat = 'food'
    )

  food_data.save()
  return render(request, 'food-poll.htm', {'res': res['meals'][0]})

def MoviesPollView(request):
  res = requests.get('https://api.themoviedb.org/3/search/movie?api_key=e82e2c2f233a83f1f733511c857285b8&query=action&page=1').json()

  for data in res['results']:
    movie_data = PollSets(
      item_name = data['original_title'],
      item_img = 'https://image.tmdb.org/t/p/w500'+data['poster_path'],
      item_cat = 'movie'
      )
    movie_data.save()
    
  return render(request, 'movies-poll.htm')

def GamesPollView(request):
  res = requests.get('https://api.rawg.io/api/games?key=193932b9cb604e338d6fe2b7d9204365&page_size=20').json()


  for data in res['results']:
    print(data['name'])

  return render(request, 'games-poll.htm')

  
class ResultsPageView(TemplateView):
  template_name = 'results.htm' 
