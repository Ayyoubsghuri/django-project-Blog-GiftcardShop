from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# from json.decoder import JSONDecodeError

import json
import datetime
from .models import *
from django.contrib import messages

# Create your views here.


@login_required(login_url='/logout')
def shop(request):
    ac = shopp.objects.get(title="Netflix")
    acsp = shopp.objects.get(title="Spotify")
    achbo = shopp.objects.get(title="Hbo")
    achulu = shopp.objects.get(title="Hulu")
    acdz = shopp.objects.get(title="Deezer")
    acno = shopp.objects.get(title="Nordvpn")
    acvy = shopp.objects.get(title="Vyprvpn")

    quantity = 0
    quantitysp = 0
    quantityhu = 0
    quantityhb = 0
    quantitydz = 0
    quantityno = 0
    quantityvy = 0
    messages = ""
    request.session['name'] = "i"
    request.session['price'] = "None"

    if ac.listacc != [""]:
        quantity = len(ac.listacc)
    if acsp.listacc != [""]:
        quantitysp = len(acsp.listacc)
    if achbo.listacc != [""]:
        quantityhb = len(achbo.listacc)
    if achulu.listacc != [""]:
        quantityhu = len(achulu.listacc)
    if acdz.listacc != [""]:
        quantitydz = len(acdz.listacc)
    if acno.listacc != [""]:
        quantityno = len(acno.listacc)
    if acvy.listacc != [""]:
        quantityvy = len(acvy.listacc)
    else:
        pass
    if request.method == "POST":
        if 'netflix' in request.POST:
            nm = "Netflix"
            pr = 1.99
        elif 'spotify' in request.POST:
            nm = "Spotify"
            pr = 1
        elif 'hulu' in request.POST:
            nm = "Hulu"
            pr = 1.5
        elif 'hbo' in request.POST:
            nm = "Hbo"
            pr = 1.5

        elif 'deezer' in request.POST:
            nm = "Deezer"
            pr = 1
        elif 'nordvpn' in request.POST:
            nm = "Nordvpn"
            pr = 1

        elif 'vyprvpn' in request.POST:
            nm = "Vyprvpn"
            pr = 1

        request.session['name'] = nm
        request.session['price'] = pr
        name = request.session['name']
        price = request.session['name']
        order = shopp.objects.get(title=name)
        if shoporder.objects.filter(acc=order.listacc[0]).exists():
            messages = "Sorry Something Wrong Show Up, Plz Try Again"
        else:
            if order.listacc[0] == "":
                messages = "You Can't Purchase this item because it's empty"
                request.session['name'] = "i"
            else:
                return redirect("../shop/payment")


    context = {
        'quantity': quantity,
        'quantitysp': quantitysp,
        'quantityhb': quantityhb,
        'quantityhu': quantityhu,
        'quantitydz': quantitydz,
        'quantityno': quantityno,
        'quantityvy': quantityvy,
        'messages': messages,
    }
    return render(request, 'shop/shop.html', context)


@login_required(login_url='/logout')
def payment(request):
    name = request.session['name']
    pric = request.session['price']
    if request.session['name'] == "i":
        return redirect("/shop")
    order = shopp.objects.get(title=name)
    if order.listacc[0] == "":
        request.session['name'] = "i"
        return redirect("/shop")

    context = {
        'name': name,
        'pric': pric,
    }
    return render(request, 'shop/payment.html', context)


# @login_required(login_url='/logout')
@csrf_exempt
def processOrder(request):
    name = request.session['name']
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if data['isPaid']:
        order = shopp.objects.get(title=name)
        acclstkamla = order.listacc
        x = acclstkamla.pop(0)
        shoporder.objects.create(
        title=order.title,
        user=request.user,
        acc=x
         )
    # messages = "Your Purchase Has Successufly Made Check Dashboard Page"
        jdidstr = '\n'.join([str(item) for item in acclstkamla])
        shopp.objects.filter(title=name).update(acc=jdidstr)


    return JsonResponse("payment Complete", safe=False)
