import form as form
from django.shortcuts import render, redirect
from .forms import ComplectForm
from .models import *


def home_page(request):
    context = {}
    return render(request,'online_delivery/home.html',context)


def products_page(request):
    hookahs = Hookah.objects.all()
    bowls = Bowl.objects.all()
    tabacco = Tabacco.objects.all()
    coals = Coals.objects.all()
    total_price = 0
    view = Complect.objects.all()
    form = ComplectForm()
    if request.method == 'POST':
        form = ComplectForm(request.POST)
        if form.is_valid():
            for product in view:
                total_price = product.hookah.price + product.bowl.price + product.tabacco.price + product.coals.price
            form.save()
    context = {'hookahs':hookahs,'bowls':bowls,'tabacco':tabacco,'coals':coals,'form':form,'total_price':total_price}
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



def complect_page(request):
    view = Complect.objects.all()
    context = {'view':view}
    return render(request,'online_delivery/complect.html',context)









