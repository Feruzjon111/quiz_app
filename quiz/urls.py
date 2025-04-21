from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/<int:baza_id>/', views.test_list, name='test_list'),
    path('create/', views.test_create, name='test_create'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.baza_list, name='baza_list'),
    path('baza/<int:baza_id>/', views.test_list, name='test_list'),
]
