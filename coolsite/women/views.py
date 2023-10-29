from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseNotFound, Http404, HttpResponseNotAllowed
from django.shortcuts import render, redirect
#для хранения представлений(контролеры) текущего приложения
# Create your views here.
from women.classurls import FourDigitYearConverter

class Car:
    def __init__(self, color):
        self.color = color

def index(request):
    print(request.GET)
    audi = Car('Black')
    data = {'title': 'Главная страница',
          'slov': {"key1": "value_1", "key2": "value_2"},
          'int': 37,
          'double': 14.7,
          'bool': False,
          'joke': sneakers,
          'menu': menu,
            }

    #return HttpResponse('главная страница women')
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'menu': menu})
def categories(request):
    return render(request, 'women/category.html',  {'menu': menu,})

def categories_id(request, catid):
    if 30 < catid < 60:
        return redirect('home')
    elif 60 < catid < 90:
        return redirect('home', permanent=True)
    elif 90 < catid < 110:
        return redirect('cat_slug', 'dfdfdf')
        # raise Http404()
    return HttpResponse(f'<h1>Статьи по номерам  {catid} </h1>')

def categories_sl(request, catid):
    return HttpResponse(f'<h1>Статьи по названиям и категориям  {catid} </h1>')

dir = {
    '1': ['Буренок Д. 2005'],
    '2': ['Горбанёв К. 2006'],
    '3': ['Капшукова Д. 2004'],
    '4': ['Климин Т. 2004'],
    '5': ['Кашаева Р. 2004'],
    '6': ['Косенков Г. 2004'],
    '7': ['Костин М. 2001'],
    '8': ['Кузенков Б. 2003'],
    '9': ['Миколодзе А. 2004'],
    '10': ['Мишин А. 2004'],
    '11': ['Мишин А. 2004'],
    '12': ['Сентюрина Е. 2002'],
    '13': ['Пешеходько А. 2004'],
}

menu = [{'title': 'Главная', 'url_n': 'home'}, {'title': 'О программе', 'url_n': 'about'},
        {'title': 'Категории', 'url_n': 'category'},
        {'title': 'Кроссовки', 'url_n': 'cross'},{'title': 'Студенты', 'url_n': 'date'}]

def cross(request):
    return render(request, 'women/cross.html',  {'joke': sneakers,'menu': menu})
def students(request, students_id):
    if students_id>0 and students_id<=10:
        return HttpResponse(f"<h1>Студент {students_id}){dir[str(students_id)][0]} найден</h1>")

    else:

        return HttpResponse(f"<h1>Студента под номеромом {students_id} нет</h1>")

def students_slug(request, students):
    return HttpResponse(f"<h1>Статья про студента{students}</h1>")

def spisok(request,key):
    return HttpResponse(f"<h1> Список участников № {dir[key]} </h1>")

date= {
        "2001": ['Костин М.'],
        "2002": ['Сентюрина Е.'],
        "2003": ['Кузенков Б.'],
        "2004": ['Капшукова Д.', 'Климин Т.', 'Кашаева Р.', 'Косенков Г.', 'Миколодзе А.', 'Мишин А.', 'Мишин А.', 'Пешеходько А.'],
        "2005": ['Буренок Д.'],
        "2006": ['Горбанёв К.'],

}
def date(request):
    dir = [
        {'FIO': 'Костин М.','HB':'2001'},
        {'FIO': 'Сентюрина Е.', 'HB':'2002'},
        {'FIO': 'Кузенков Б.', 'HB':'2003'},
        {'FIO': 'Капшукова Д.','HB':'2004'},
        {'FIO': 'Климин Т.', 'HB': '2004'},
        {'FIO': 'Кашаева Р.', 'HB': '2004'},
        {'FIO': 'Косенков Г.', 'HB': '2004'},
        {'FIO': 'Миколодзе А.', 'HB': '2004'},
        {'FIO': 'Мишин А.', 'HB': '2004'},
        {'FIO': 'Мишин А.', 'HB': '2004'},
        {'FIO': 'Пешеходько А.', 'HB': '2004'},
        {'FIO': 'Буренок Д.','HB':'2005'},
        {'FIO': 'Горбанёв К.','HB':'2006'},
    ]
    return render(request,'women/students.html',{'date':dir,'menu':menu,})

def getStr(request):
    if(request.GET):
        result = str()
        for key in request.GET:
            result += key + ": " + request.GET[key] + ", "
        return HttpResponse(f"<h2>Get-запрос</h2> <p>Запрос: {result}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1> Страница не найдена </h1>")

def badRequest(request, exception):
    return HttpResponseBadRequest(f"Bad Request")

def forbiden(request, exception):
    return HttpResponseForbidden(f"Forbiden")

def serverError(request, exception):
    return HttpResponseServerError(f"ServerError")

def year_sl(request, year):
    if year > 2000 or year < 2023:
        return HttpResponse(f"<h1> год  {year} - война </h1>")
def year(request, year):
    if year > 2000 or year < 2023:
        return HttpResponse(f"<h1> год  {year} - война </h1>")

def stup(request,axe):
    if 1990 < axe < 2000:
        return redirect('home')
    elif 2000 < axe < 2023:
        return redirect('home', permanent=True)
    elif 2023 < axe < 2050:
        return redirect('students', 1)


sneakers =[
    {'id': 1, 'brend': 'Nike', 'model': 'SB', 'sold': True},
    {'id': 2, 'brend': 'Adidas', 'model': 'campus', 'sold': True},
    {'id': 3, 'brend': 'Diadora', 'model': 'Camo', 'sold': True},
    {'id': 4, 'brend': 'Raf', 'model': 'hover', 'sold': False},
    {'id': 5, 'brend': 'Puma', 'model': 'sueda', 'sold': False},
]
def post_detail(request):
    if(request.GET):
        if len(request.GET) > 0:
            parameters = ''
            for key, value in request.GET.items():
                parameters += f"{key}={value}|"
            parameters = parameters[:-1]  # удаляем вертикальную черту в конце
            return HttpResponse(parameters)
    else:
        return HttpResponse("GET is empty")
