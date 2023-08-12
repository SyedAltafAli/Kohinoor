from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Kohinoor Catters"
admin.site.site_title = "Kohinoor Catters Admin Portal"
admin.site.index_title = "Welcome to Kohinoor Catters"


urlpatterns = [
    path("", views.index, name='About'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'), 
]