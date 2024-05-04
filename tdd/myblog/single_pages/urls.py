from django.urls import path
from single_pages.views import about_me, landing

app_name = 'single_pages'

urlpatterns = [
    path('', landing, name='landing'),
    path('about_me/', about_me, name='about_me')
]