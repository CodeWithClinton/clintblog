from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog/<str:slug>', views.readmore, name = 'readmore')
]