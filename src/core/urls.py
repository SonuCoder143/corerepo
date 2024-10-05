
from django.contrib import admin
from django.urls import path
from firstapp import views as s1
from secondapp import views as s2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',s1.firstView,name="firstview"),
    path('second/',s1.secondView,name="secondview"),
    path('third/',s2.thirdView,name="thirdview"),
    path('fourth/',s2.fourthView,name="fourthview"),
]
