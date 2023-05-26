from django.urls import path
from blood import views

urlpatterns = [
    path('',views.index, name="index"),
]