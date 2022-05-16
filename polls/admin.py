from django.contrib import admin

from polls.models import PollSets

admin.site.site_header = 'Pollarize Admin'

# Register your models here.

admin.site.register(PollSets)