import requests
import time
from django.shortcuts import render, redirect
from .models import zearch
from bs4 import BeautifulSoup

# site lien
# Create your views here.


def zearch_vi(request):
    if request.method == "GET":
        var = request.GET.get('search')
        v = str(var)
        ss = v.replace(" ", "+")
        result = requests.get("http://udemydownloader.net/?s=" + ss)
        result2 = requests.get("https://www.classcentral.com/search?q=" + ss)
        src = result.content
        src2 = result2.content
# n7wloh ltari9a bach yt9ra lsysteme
        soup = BeautifulSoup(src, "lxml")
        soup2 = BeautifulSoup(src2, "lxml")
# nakhdo ach bghina mn site
        titlee = soup.find_all("a", {"class": "post-title post-url"})
        titlee2 = soup2.find_all(
            "span", {"class": "text-1 weight-semi line-tight"})

        urll = soup.find_all("a", {"class": "read-more"})
        urll2 = soup2.find_all(
            "a", {"class": "color-charcoal block line-tight course-name"})

        href = []
        href2 = []

        # list_for_random = range(2, 5)
        for u in urll:
            href.append(u.get('href'))
        for ui in urll2:
            href2.append("https://www.classcentral.com" + ui.get('href'))
        for i in range(len(titlee)):
            if zearch.objects.filter(title=titlee[i].text.strip()).exists():
                pass
            else:
                zearch.objects.create(
                    title=titlee[i].text.strip(),
                    url=href[i]
                )
        for i in range(len(titlee2)):
            if zearch.objects.filter(title=titlee2[i].text.strip()).exists():
                tt = zearch.objects.filter(title__icontains=v)
            else:
                zearch.objects.create(
                    title=titlee2[i].text.strip(),
                    url=href2[i]
                )
        tt = zearch.objects.filter(title__icontains=v)
        context = {
            'tt': tt,
        }
    return render(request, 'search/search.html', context)
