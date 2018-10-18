from django.urls import path
from . import views

urlpatterns = [
    path('', views.perris_list, name='perris_list'),
]
