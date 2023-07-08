from django.http import HttpResponse
from django.shortcuts import render
from .models import Book , User
from .forms import book_form

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    query = request.GET.get('query')
    genre = request.GET.get('genre')
    max_price = request.GET.get('max_price')
    max_date = request.GET.get('max_date')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains = query) | books.filter(author__icontains = query) | books.filter(genre__icontains = query)
    if genre:
        books = books.filter(genre = genre)
    if max_price:       
        books = books.filter(price__lte = max_price)
    if max_date:
        books = books.filter(publication_date__lte = max_date)

    return render(request , 'bookstore/index.html',{'books':books ,'current_user':request.user})

@login_required(login_url="/login")
def add_book(request):
    if request.method == "POST":
        form=book_form(request.POST)
        if form.is_valid():
            # form.instance.author = request.user
            form.save()
            messages.success(request,"Book succesfully added.")
            return HttpResponseRedirect(reverse("index"))  

        else:
            messages.error(request,"Oops!! an error occured while saving ,Try again.")
            return HttpResponseRedirect(reverse('add_book'))

    return render(request,"bookstore/create.html",{"form":book_form()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request,"Invalid username and/or password.")
            return render(request, "bookstore/login.html")
    else:
        return render(request, "bookstore/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, 'Passwords Must Match.')
            return render(request, "bookstore/register.html")

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request,"Username already taken.")
            return render(request, "bookstore/register.html")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bookstore/register.html")
    

@login_required(login_url="/login") 
def update_cart(request,id):
    if request.method=="POST":
        user=request.user
        book=Book.objects.get(pk=id)
        if book in  Book.objects.filter(is_in_cart=request.user).all(): # or book.is_in_cart(user)
            book.is_in_cart.remove(user)
            messages.info(request, 'removed from Cart')
        else:
            book.is_in_cart.add(user)
            messages.info(request, 'added to cart')
    return HttpResponseRedirect(reverse('index'))
    

@login_required(login_url='/login')
def remove_cart(request,id):
    if request.method=="POST":

        book=Book.objects.get(pk=id)

        user=request.user

        # user.watchlist.remove(listing)
        book.is_in_cart.remove(user)

        messages.success(request,"Removed from Cart.")
    return HttpResponseRedirect(reverse('cart'))

@login_required(login_url="/login") 
def cart(request):
    return render(request,'bookstore/cart.html',{
        "cart":Book.objects.filter(is_in_cart=request.user).all()
    })


