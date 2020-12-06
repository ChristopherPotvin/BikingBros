from django.urls import path
from . import views

#Url patterns request URL
app_name="apitest"
urlpatterns = [
   path("", views.index, name="index")
]