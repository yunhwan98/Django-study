from django.contrib import admin
from django.urls import path, include #include를 import
from myapp import views


urlpatterns = [#사용자가 들어온 경로 적기
    path('',views.index),   #view.index로 위임
    path('create/',views.create),
    path('read/<id>/', views.read),
    path('delete/', views.delete)   #delete로 위임
]
