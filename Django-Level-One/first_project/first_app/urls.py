from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
   # re_path(r"^$", views.index, name="index"),
]
