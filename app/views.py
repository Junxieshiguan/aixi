from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return redirect(reverse('app:home'))


def home(request):
    return render(request,'home.html')


def market(request):
    return render(request,'market.html')


def cart(request):
    return render(request,'cart.html')


def mine(request):
    return render(request,'mine.html')


