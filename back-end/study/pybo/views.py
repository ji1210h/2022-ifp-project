from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("안녕하세요! pybo에 온 것을 환영해요 =ㅂ=")
