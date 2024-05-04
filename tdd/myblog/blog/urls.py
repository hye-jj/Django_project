from django.urls import path
from blog.views import PostDetail, PostList # index, single_post_page,

app_name = 'blog'

urlpatterns = [
     path('<int:pk>/', PostDetail.as_view()),
     path('', PostList.as_view()),
     # path('', index, name='index'),
     # path('<int:pk>/', single_post_page, name='single_post_page'),
]