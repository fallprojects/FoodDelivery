from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',home_page,name='home'),
    path('products/',products_page,name='products'),
    path('actions/',action_page,name='actions'),
    path('adresses/',contact_page,name='contacts'),
    path('comments/',comment_page,name='comments'),
    path('purchase/<int:pk>/',purchase,name='purchase')
]
