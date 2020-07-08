from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('<h1>Hello world !</h1>')

def test(response):
    return HttpResponse('<h1>Тестовая страница</h1>')
    
    
