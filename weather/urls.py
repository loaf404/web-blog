from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.say_hello),
    path('hello/', views.Nothing),
    path('test/', views.testing),
    path('weatherM/', views.Weather),
    #blog url path
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('board/', views.board, name='board'),
    path('index-c/', views.index_c, name='index-c'),
]