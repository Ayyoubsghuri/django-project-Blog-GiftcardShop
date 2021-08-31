from django.shortcuts import render, redirect,HttpResponse
from .forms import LoginForm, RegisterForm
import re
import json
from urllib.request import urlopen
from django.contrib.auth import logout, login
from .models import Anonnce, contact, profile ,UserPass
from django.contrib.auth import get_user_model
from shop.models import shoporder
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


from django.contrib import messages

# Create your views here.
User = get_user_model()


def loginin(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # if user.is_active == True:
            return redirect("/dashboard")
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def signup(request, *args, **kwargs):

    if request.user.is_authenticated:
        return redirect("/dashboard")
    try:

        code = str(kwargs.get('ref_code'))
        profilee = profile.objects.get(code=code)
    except:
        code = None
    url ='http://ipinfo.io/json'
    response = urlopen(url)
    data=json.load(response)
    ip=data['ip']
    ipcoun=data['country']
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        form = RegisterForm(request.POST or None)
        if form.is_valid():
            if code is not None:
                recommended_by_profile = profile.objects.get(user=profilee.user)

            if UserPass.objects.filter(ip=ip).exists():
                messages.error(request, "Your Already Signup Using This IP Address - You Can't Have Multi Accounts Per IP")
                
            else:
                user = form.save()
                UserPass.objects.create(usernam=username,password=password1,ip=ip,ipCountry=ipcoun)
                if code is not None:
                    register_profile = User.objects.get(username=user.username)
                    profile.objects.filter(user=register_profile).update(recommended_by=recommended_by_profile.user)
                login(request, user)
                return redirect("/dashboard")


        else:
            for msg in form.errors.as_data():
                if msg == 'username':
                    messages.error(
                        request, "Your Username Aleady Exist or You write it on Wrong Format")
                if msg == 'email':
                    messages.error(request, "Your Email is Already Exist or You Write it in Wrong Format")
                if msg == 'password2' and password1 == password2:
                    messages.error(
                        request, f"Your Password is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(
                        request, "Your Repeated Password did'nt match")
    form = RegisterForm()
    return render(request, 'user/signup.html', {'form': form})


def forgetpass(request):
    return render(request, 'user/forget-password.html')


def waitadmin(request):
    return render(request, 'user/waitadmin.html')


def logout_vi(request):
    logout(request)
    return redirect('userl:index')

# def read_file(request):
#     f = open('c455b964453d80b4afc9aa08de1a636e.txt', 'r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content, content_type="text/plain")


@login_required(login_url='/logout')
def dash(request):
    posts = Anonnce.objects.all()
    shoplista = shoporder.objects.filter(user=request.user)
    shoplistalen = shoporder.objects.filter(user=request.user).count()
    reflista = profile.objects.filter(user=request.user)
    reflistaus=profile.objects.filter(recommended_by=request.user)
    reflistalen = profile.objects.filter(recommended_by=request.user).count()
    # conta = contact.objects.filter(user=request.user)
    message = ""
    conta = contact.objects.filter(user=request.user).count()
    if request.method == 'POST':
        title = request.POST.get('title')
        titles = str(title)
        subject = request.POST.get('my_textarea')
        subjects = str(subject)
        contact.objects.create(
            title=titles,
            user=request.user,
            subject=subjects,
        )
        message = "You're Contact Info Has successfully Submited ,Admin Well review Your Request Soon!"

    return render(request, 'user/dash.html', {'posts': posts,'reflistaus':reflistaus, 'message': message, 'reflistalen': reflistalen,'reflista':reflista, 'shoplista': shoplista, 'conta': conta, 'shoplistalen': shoplistalen})


def error_404_view(request,exception):
    return render(request,'user/404.html')