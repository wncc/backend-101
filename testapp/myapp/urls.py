from django.contrib import admin
from django.urls import include, path
from .views import ItemView, test

urlpatterns = [
    path('test', test, name='test'),
    path('', ItemView.as_view(), name='home'),

]