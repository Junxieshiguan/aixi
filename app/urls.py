#name:urls
#author:Yangwenwu
#@Time:2018/7/24 19:46
from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^home/', views.home,name='home'),
    url(r'^market/', views.market,name='market'),
    url(r'^cart/', views.cart,name='cart'),
    url(r'^mine/', views.mine,name='main'),
]
