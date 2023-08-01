from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Ответ отправлен!')

# Create your views here.
