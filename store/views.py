from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models.category import Category
from .models.product import Product

# Create your views here.
def home(request: HttpRequest):
    if request.method == 'POST':
        product = request.POST.get('product')
        operation = request.POST.get('operation')

        cart = request.session['cart']
        quantity = cart.get(product, 0)
        if operation == "remove":
            if quantity == 1:
                cart.pop(product)
            else:
                cart[product] = quantity-1
        else:
            cart[product] = quantity+1
        
        request.session['cart'] = cart

    return redirect("store")

### store view
def store(request: HttpRequest):
    # cart
    if not request.session.get('cart'):
        request.session['cart'] = {}

    # get product by category
    categoryId = request.GET.get('category')
    products = None
    if categoryId:
        products = Product.objects.filter(category=categoryId)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    return render(request, 'home.html', {"categories": categories, "products": products})


### cart view
def cart(request: HttpRequest):
    cart = request.session['cart']
    products = [Product.objects.filter(id=prod[0]).first() for prod in cart]
    # print(products)
    return render(request, 'cart.html', {"products": products})

### login view
def login(request):
    return render(request, "login.html")

### signup view
def signup(request):
    return render(request, "signup.html")
