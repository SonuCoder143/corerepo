from django.urls import path
from secondapp import views as v1

urlpatterns = [
    path("third",v1.thirdView),
    path("fourth",v1.fourthView),
]
