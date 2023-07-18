from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("city", views.city, name='city'),
    path("usa", views.usa, name='usa'),
    path("uae", views.uae, name='uae'),
    path("gotham", views.gotham, name='gotham'),
    path("london", views.london, name='london'),
    path("canada", views.canada, name='canada'),
    path("NorthKorea", views.NorthKorea, name='NorthKorea'),
]
