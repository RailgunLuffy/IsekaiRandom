from django.urls import path

from . import views

app_name = 'isekai'
urlpatterns = [
    path('', views.home, name="home"),
    path('random/', views.result, name="result"),
]