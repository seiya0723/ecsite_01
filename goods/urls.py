from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('', views.groupcreate, name='group_create'),
    path('goods_create', views.goodscreate, name='goods_create')
]
