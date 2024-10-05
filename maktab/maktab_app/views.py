from django.shortcuts import render
import telebot
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request,'6-IDUM.html')