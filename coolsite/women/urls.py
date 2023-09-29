from django.urls import path

from women.views import *

urlpatterns = [

    path('', index),
    path('cat/', categories),
    path('cat/<int:catid>/', categories_id),
    path('cat/<slug:catid>/', categories_sl),


]