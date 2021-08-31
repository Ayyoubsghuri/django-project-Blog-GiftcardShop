from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Post ,PostVIP
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from django.views.decorators.http import require_GET, require_POST
# from django.http import Http404




# Create your views here.
@login_required(login_url='/logout')
def blog(request):
    artiss = Post.objects.all()
    artissvip = PostVIP.objects.all()
    paginator = Paginator(artiss,1)
    page =request.GET.get('page')
    artis=paginator.get_page(page)

    paginator = Paginator(artissvip,1)
    page =request.GET.get('page')
    artisvip=paginator.get_page(page)
    
    context = {
        'artis':artis,
        'artisvip':artisvip,
    }
    return TemplateResponse(request, 'blog/blog.html', context)

@login_required(login_url='/logout')
def id(request,slug):
    arti = Post.objects.get(slug=slug)

    context = {
        'arti':arti,
    }
    return TemplateResponse(request,'blog/blogid.html',context)

@login_required(login_url='/logout')    
def idvip(request,slug):
    artivip = PostVIP.objects.get(slug=slug)

    context = {
        'artivip':artivip,
    }
    return TemplateResponse(request,'blog/blogidv.html',context)  

