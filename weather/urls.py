from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index, name='index'),
    #blog url path
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('board/', views.board, name='board'),
]