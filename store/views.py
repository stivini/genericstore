from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Products, Users, Category, DefaultImages
from .forms import UsersForm, ProductsForm
from django.views.generic import DetailView
from django.contrib import messages

default_thumbnail = DefaultImages.objects.get(name__startswith='default')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            # Redirect to a success page.
            return redirect('/store/products/')
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'log.html')

def wishlist(request):
    return render(request, 'wishlist.html')
    
def sign_in(request):
    if request.method=='POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            id = form.cleaned_data['id']
            email = form.cleaned_data['email']
            password  = form.cleaned_data['password']
            thisuser = Users(firstname=first_name, lastname=lastname, phone=phone, ids=id, email=email, password=password)
            thisuser.save()
            return render(request, 'tests.html')
    else:
        form = UsersForm()
    return render(request, 'tests.html', {'form':form})

def products(request):
    data = Products.objects.all()
    return render(request, 'products.html', {'data':data, 'default_thumbnail':default_thumbnail})

def cart(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
    #user = get_object_or_404(Users, username=logged_in_user)
    user = Users.objects.get(username=logged_in_user)
    #product = Products.objects.all()
    user_products = user.products.all()

    context = Products.objects.all()
    users = Users.objects.all()
    total = total_to_checkout()
    return render(request, 'cart.html', {"context":context, "total":total, 'default_thumbnail':default_thumbnail, 'users':users, "logged_in_user":logged_in_user, 'user_products':user_products})


    
def spesscat(request,name):
    info = get_object_or_404(Category, name=name)
    prods = Products.objects.filter(category=info)
    return render(request, 'spesscat.html', {'info':info, 'prods':prods})

def remove(request,name):
    if request.user.is_authenticated:
        logged_in_user = request.user
    
    info = Products.objects.get(name=name)
    user = Users.objects.get(username=logged_in_user)
    user.products.remove(info)

    info.order_amount = 0
    info.cart = False
    info.save()
    return cart(request)

	
def spesproducts(request,name):
    # takes name from database to use as a product url
    if request.user.is_authenticated:
        logged_in_user = request.user

    info = Products.objects.get(name=name)
    active_user = Users.objects.get(username=logged_in_user)
    active_user.products.add(info)
    

    if request.method=='POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            amt = form.cleaned_data['amount']
            info.cart = True
            info.order_amount=amt
            info.save()
            return cart(request)
    else:
        form = ProductsForm()
    return render(request, 'product2.html', {'info':info, 'form': form, 'default_thumbnail':default_thumbnail, 'logged_in_user':logged_in_user})

def login(request):
    if request.method=='POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            password  = form.cleaned_data['password']
            return render(request, 'login.html', {
                "first_name":first_name,
                'password':password,
                })
    else:
        form = UsersForm()
    return render(request, 'login.html', {'form': form})


def category(request):
    data = Category.objects.all()
    return render(request, 'category.html', {'data':data})

def test(request):
	return render(request, 'modeltemp.html')
	
def profile(request):
    
	return render(request, 'profile.html')
	
def checkout(request):	
    item = Products.objects.all()
    return render(request, 'my_app:index.html')

def total_to_checkout():
    pass
    # multiplies amount by selling price
    # adds subtotals together for full price checkout
    data = Products.objects.values_list('order_amount', 'sellp')
    result = []
    for nested_tuple in data:
        multiply = nested_tuple[0]*nested_tuple[1]
        result.append(multiply)
    ans = sum(result)
    return int(ans)

def purchase_product(request, username, name):
    product = get_object_or_404(Products, name=name)
    user = get_object_or_404(Users, username=username)

    if product.order_amount > 0 and product.quantity > 0:
        # Perform the purchase logic here, for example, updating product quantity and user's purchased products
        product.order_amount -= 1
        product.quantity_in_stock -= 1
        product.save()

        # Add the purchased product to the user's products using the foreign key relationship
        user.products.add(product)
        user.save()

        messages.success(request, f'You have successfully purchased {product.name}.')
    else:
        messages.error(request, f'Sorry, {product.name} is out of stock.')

    # Redirect the user back to the product detail page after the purchase attempt
    return render(request, 'product_detail.html', {'product': product, 'user': user})