from django.shortcuts import render
import telebot
from django.shortcuts import redirect
from .models import Blog

# Create your views here.

bot = telebot.TeleBot("7835800080:AAEp9JjZyMjTAhU2Cptdjb51w57Oilvdc9s", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


def home(request):
    return render(request,'6-IDUM.html')

def contact(request):
    name = request.GET.get("name")
    number = request.GET.get("number")
    email = request.GET.get("email")
    text = request.GET.get("message")


    if name is not None:
        message = f""" 
        massage:
        name: {name}
        phone: {number}
        email: {email}
        text: {text}
        """
        bot.send_message(7189884017, message)
        return redirect('contactPage')

    return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, "blog.html", {"blogs":blogs})

def about(request):
    return render(request,'about.html')