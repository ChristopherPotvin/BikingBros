import include
from django.urls import path
from.import views

#Url patterns request URL
urlpatterns = [
   path("", views.index, name="index")
]