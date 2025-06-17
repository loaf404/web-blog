from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

# blog html

def contact(request):
    return render(request, "weather/contact.html")

def index(request):
    return render(request, "weather/index.html")

def projects(request):
    return render(request, "weather/projects.html")

def resume(request):
    return render(request, "weather/resume.html")

def board(request):
    boards = Board.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            new_board = Board(title=title, content=content)
            new_board.save()
            return redirect('board')
    return render(request, "weather/board.html", {'boards': boards})



# To run the server, write down "python manage.py runserver"