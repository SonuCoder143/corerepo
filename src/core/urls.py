
from django.contrib import admin
from django.urls import path,include
from firstapp import views as v3


urlpatterns = [
    path("",v3.homeview),
    path('admin/', admin.site.urls),
    path("firstapp/",include("firstapp.urls")),
    path("secondapp/",include("secondapp.urls")),
]
