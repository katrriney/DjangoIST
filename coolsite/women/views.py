from django.http import HttpResponse
from django.shortcuts import render
# для хранения представлений(контролеров) текущего приложения
# Create your views here.


def index(request):
    return HttpResponse('главная страница women')

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')