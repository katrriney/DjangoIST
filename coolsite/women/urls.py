from django.urls import path, register_converter

from women.classurl import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index),
    path('cat/', categories),
    path("articles/<yyyy:year>/", year_archive),
    path('cat/<int:catid>/', categories_id),
    path('cat/<slug:catid>/', categories_sl),

]
