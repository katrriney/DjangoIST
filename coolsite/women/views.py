from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


# для хранения представлений(контролеров) текущего приложения
# Create your views here.


def index(request):
    if (request.GET):
        print(request.GET)
    return HttpResponse('главная страница women')


def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')


def categories_id(request, catid):
    if int(catid) > 30:
        raise Http404()

    return HttpResponse(f'<h1>Статьи по номерам  {catid}</h1>')


def categories_sl(request, catid):
    return HttpResponse(f'<h1>Статьи по названиям и категориям {catid}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Статьи не найдена</h1>')


def year_archive(request, year):
    if int(year) > 2023 or  int(year) < 2000:
        raise Http404()

    return HttpResponse(f'<h1>В этот год случилось  {year}</h1>')
