from django.urls import path
from firstapp import views as v


urlpatterns = [
    path("first",v.firstView),
    path("second",v.secondView),
]
