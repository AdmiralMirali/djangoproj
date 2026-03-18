from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # Главная страница
    path('', views.index, name = 'index'),
    # Страница со списком постов
    #path('posts', views.ice_cream_list),
    # Отдельная страница с информацией о сорте мороженого
    #path('posts/<pk>/', views.ice_cream_detail),
    #path('group/<slug:name>', views.group_posts)
]