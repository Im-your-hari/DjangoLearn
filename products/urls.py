from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    #path('contactform/',views.contact_create_view,name="contact_form"),
    path(r'products/',views.products_details,name="productsa"),
    path('create/',views.create,name="create"),

]
