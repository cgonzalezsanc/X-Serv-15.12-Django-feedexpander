from django.shortcuts import render
from django.http import HttpResponse
from models import Tweet
from bs4 import BeautifulSoup
import urllib
import feedparser


# Create your views here.

def handler(request, username):
    url = 'http://twitrss.me/twitter_user_to_rss/?user=' + username
    dicc = feedparser.parse(url)
    salida = "<html>\n\t<body>\n\t\t"
    for tweet_num in range(5):
        content = dicc.entries[tweet_num].title
        salida += content + "<br>\n\t\t"
        t = Tweet(content=content, url=dicc.entries[tweet_num].link)
        t.save()
        salida += "Lista de URLs: <br>\n\t\t\t"
        for url_num in range(1, len(content.split("http://"))):
            url = "http://" + content.split("http://")[url_num].split(" ")[0]
            salida += url + "<br>\n\t\t\t"
            html = urllib.urlopen(url)
            html_doc = html.read()
            soup = BeautifulSoup(html_doc)
            print soup.p
            salida += "-Texto del primer elemento: " + str(soup.p)
            salida += "<br>\n\t\t\t-Imagenes:<br>\n\t\t\t"
            for img in soup.find_all('img'):
                salida += str(img) + "<br>\n\t\t\t"
        salida += "<br>\n\t\t"
    salida += "\n\t</body>\n</html>"
    return HttpResponse(salida)
