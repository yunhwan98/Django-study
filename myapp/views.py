from django.shortcuts import render,HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome!</h1>'+str(random.random())) #random한 페이지 생성 예시

def create(request):
    return HttpResponse('Create!') #http를 이용한 객체전달
def read(request,id):
    return HttpResponse('Read!'+id) #http를 이용한 객체전달