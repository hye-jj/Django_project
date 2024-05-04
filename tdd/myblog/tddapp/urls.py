from django.urls import path
from tddapp.views import detail

app_name = 'tddapp'

urlpatterns = [
    path('detail/', detail, name='detail')
]