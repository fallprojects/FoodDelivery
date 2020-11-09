from django.shortcuts import render
from .models import *


def home_page(request):
    context = {}
    return render(request,'online_delivery/home.html',context)


def products_page(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request,'online_delivery/product.html',context)


def contact_page(request):
    adresses = Adresses.objects.all()
    context = {'contact_page': adresses}
    return render(request,'online_delivery/contacts.html',context)

def comment_page(request):
    comments = Comments.objects.all()
    context = {'comment_page': comments}
    return render(request,'online_delivery/comments.html',context)

def action_page(request):
    actions = Actions.objects.all()
    context = {'action_page': actions}
    return render(request,'online_delivery/actions.html',context)