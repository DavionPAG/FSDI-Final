from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.htm'

class AboutPageView(TemplateView):
  template_name = 'about.htm'

class PollPageView(TemplateView):
  template_name = 'poll.htm'

class ResultsPageView(TemplateView):
  template_name = 'results.htm' 
