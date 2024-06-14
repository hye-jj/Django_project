from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    # path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
    # path('liked-photos/', views.liked_photos, name='liked_photos'),

    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('like/', views.liked_posts, name='liked_posts'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # 로그아웃 URL 패턴
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
]

