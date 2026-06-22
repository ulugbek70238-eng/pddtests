from django.shortcuts import render, redirect
from .models import Category, Product, Cart
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import RegForm
from django.views import View
import telebot
bot = telebot
# Create your views here.
def home_page(request):
    # Достаем данные из БД
    categories = Category.objects.all()
    products = Product.objects.all()
    # Передаем данные на Frontend
    context = {"categories": categories, "products": products}
    return render(request, 'home.html', context)

def category_page(request, pk):
    # Достаем данные из БД
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)
    # Передаем данные на Frontend
    context = {"category": category, "products": products}
    return render(request, 'category.html', context)

def product_page(request, pk):
    # Достаем данные из БД
    product = Product.objects.get(id=pk)
    # Передаем данные на Frontend
    context = {"product": product}
    return render(request, 'product.html', context)

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = RegForm
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
            return redirect('/')

def search(request):
    if request.method == 'POST':
        searched_product = request.POST.get('search_product')
        product = Product.objects.filter(product_name__iregex=searched_product)
        context = {}
        if product:
            context.update(user_pr=searched_product, products=product)
        else:
            context.update(user_pr=searched_product, products='')
        return render(request, 'result.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def add_to_cart (request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        user_amount = int(request.POST.get('pr_amount'))
        if i <= user_amount

def del_from_cart(request, pk):
    Cart.objects.filter(user_product=Product.object.get(id=pk)).delete()
    return redirect('/')

def cart_page(request):
    user_cart = cart.obgects.filter(user_product=Product.object.get())
    total = [round(t.user_pr_amount * t.user_product.product_price, 2) for t in user_cart]
    context = {}
    if user_cart
        context.update(cart=user_cart, total=round(sum(total), 2))
    else:
        context.update(cart="", total=0)
        if request.method == 'POST':
            text = f'Новый заказ!\n Клиент: {user.object.get(id=request.user.id)}.email\n\n'
            for i in user_cart:
                product = Product.objects.get(id=i.product.id)
                user_amount = int(request.POST.get(f'amount_'))
    return render(request, 'cart.html', context)


