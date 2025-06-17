from django.shortcuts import render, redirect
from .models import Board
from django.http import HttpResponse
import time
# Create your views here.

def say_hello(request):
    return render(request, "weather/hello.html")

def Nothing(request):
    return HttpResponse("Testing")

def testing(request):
    Loantime = time.time()
    Rt = time.localtime(Loantime)
    FormattedRt = time.strftime("%Y년 %m월 %d일 %H시 %M분 %S초", Rt)
    number = range(1,11)
    return render(request, "weather/testing.html", {'time': FormattedRt, 'number': number})

def Weather(request):
    return render(request, "weather/Main.html")


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

def index_c(request):
    return render(request, "weather/index-c.html")



# To run the server, write down "python manage.py runserver"