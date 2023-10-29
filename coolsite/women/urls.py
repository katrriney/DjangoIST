from django.urls import path,register_converter

from women.classurls import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cat/', categories, name='category'),
    path("articles/<yyyy:year>/",year, name='articles'),
    path('cat/<int:catid>/', categories_id, name='cat'),
    path('cat/<slug:catid>/', categories_sl, name='cat_slug'),
    path('students/<int:students_id>/', students, name='students'),
    path('students/<slug:students>/', students_slug),
    path("spisok/<int:key> ", spisok),
    path('date/', date, name='date'),
    path('stup/<int:axe>/', stup),
    path('GET/', getStr, name='getStr'),
    path('GET_1/', post_detail, name='post_detail'),
    path('cross/', cross, name='cross'),
]

