from django.urls import re_path
from.import views

#Url patterns request URL
urlpatterns = [
   path("", views.index, name="index") ,
]