from django.shortcuts import render
from django.http import HttpResponse
from models import Tweet
from models import Persona
import feedparser


# Create your views here.

def handler(request, username):
    url = 'https://twitrss.me/twitter_user_to_rss/?user=' + username
    dicc = feedparser.parse(url)
    salida = ""
    p = Persona(name=username)
    p.save()
    for number in range(5):
        salida += dicc.entries[number].title + '<br>\n'
        t = Tweet(content=dicc.entries[number].title,
                  url=dicc.entries[number].link, name=p)
        t.save()
    return HttpResponse(salida)