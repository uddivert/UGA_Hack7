from django.contrib import admin
from django.urls import path
from webApp.login.views import login
from webApp.home.views import home
from webApp.register.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('home/', home),
    path('register/', register)
]
