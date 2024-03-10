from django.urls import path
# Импортируем созданные нами представления
from .views import (
    PostsList, PostDetail, NewsCreate, NewsUpdate, NewsDelete, PostSearch,
    ArticlesCreate, ArticlesUpdate, ArticlesDelete, CategoryListView, subscribe
)

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),

    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),

    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]