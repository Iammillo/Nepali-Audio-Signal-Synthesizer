from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='abc'),
    path('request/',views.tempo,name="cde"),
]
