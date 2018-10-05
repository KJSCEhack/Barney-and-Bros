from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', upload_csv, name="uploadcsv"),
    path('email/', email, name="email"),
    path('dashboard/', dashboard, name="dashboard"),
    path('user/', user, name="user"),
    path('table/', table, name="table"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]
