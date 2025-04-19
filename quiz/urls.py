from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='custom_logout'),
    path('', views.index, name='index'),
    path('tests/', views.test_list, name='test_list'),
    path('create/', views.test_create, name='test_create'),
]
