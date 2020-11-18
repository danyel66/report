from django.urls import path
from .views import index, basicTable

urlpatterns = [
    path('', index, name='index'),
    path('basic-table/', basicTable, name='basic-table'),

]