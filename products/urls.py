from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.home),
    path('about/',views.about),
    path('contact/',views.contact),

]
