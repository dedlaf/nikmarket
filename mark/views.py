from django.shortcuts import render,redirect
from .models import UserProfile, Order, Product, Cart, CartItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, TaskForm, RegForm
from django.http import JsonResponse



def index(request):
    try:
        user = request.user
        product = Product.objects.all()
        data = {'products':product, 'cartitem':CartItem.objects.filter(cart=user.id), 'user':user, 'cart':Cart.objects.get(user=user.id)}

    except:
        data = {'products':product}
    return render(request, 'mark/main.html',data)


def auth(request):
    if request.method == 'POST':
        login1 = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=login1, password=password)
        if user is not None:
            login(request, user)
            print('Login successful')
            # Выведите алерт или перенаправьте пользователя на другую страницу
            return redirect('/')  # Замените 'home' на нужный URL

    return render(request, 'mark/auth.html')

def register(request):
    if request.method == 'POST':
        # Получите данные из формы
        login = request.POST.get('username')
        password = request.POST.get('password')
        print(login, '14314')
        email = request.POST.get('email')
        # Создайте пользователя
        user = User.objects.create_user(username=login, password=password)
        # Создайте профиль пользователя
        user_profile = UserProfile.objects.create(user=user)
        # Перенаправьте пользователя на другую страницу (например, на страницу входа)
        return redirect('/auth')


    return render(request, 'mark/register.html', {'form': RegForm()})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile')  # Замените 'profile' на нужный URL страницы профиля
    else:
        form = ProfileForm(instance=user)
    # Получите данные о пользователе
    orders = Order.objects.filter(user=user.id)

    context = {
        'user': user,
        'orders': orders,
        'form': form,
    }

    return render(request, 'mark/profile.html', context)


def profile_admin(request):
    return render(request, 'mark/profile-admin.html')

def logouting(request):
    logout(request)
    return redirect('/auth')


def cart(request):
    for i in CartItem.objects.all():
        if i.quantity == 0:
            print(i)
            i.delete()
    user = request.user
    try:
        total = 0
        for i in CartItem.objects.filter(cart=Cart.objects.filter(user=user)[0]):
            total += i.product.price*i.quantity
        print(total)
        data = {'cart':CartItem.objects.filter(cart=Cart.objects.filter(user=user)[0]), 'user': user, 'prods': Product.objects.all(), 'total': total}
    except:
        data = {'user': user}
    return render(request, 'mark/cart.html', data)


def add_to_cart(request, product_id):
    if request.method == 'PUT':
        # Получите товар по его ID
        product = Product.objects.get(pk=product_id)
        print(product)
        # Получите корзину пользователя (предполагается, что пользователь авторизован)
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        # Создайте или обновите связь между товаром и корзиной
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        cart_item.quantity += 1
        cart_item.save()

        return JsonResponse({'message': 'Товар успешно добавлен в корзину'})

    return JsonResponse({'message': 'Неверный метод запроса'}, status=400)


def min_to_cart(request, product_id):
    if request.method == 'PUT':


        # Получите товар по его ID
        product = Product.objects.get(pk=product_id)
        print(product)
        # Получите корзину пользователя (предполагается, что пользователь авторизован)
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        # Создайте или обновите связь между товаром и корзиной
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)

        cart_item.quantity -= 1
        cart_item.save()


        return JsonResponse({'message': 'Товар успешно добавлен в корзину'})

    return JsonResponse({'message': 'Неверный метод запроса'}, status=400)


def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES.get('image')
            print(image)
            form.image = image
            form.save()
            return redirect('/task')
        title = request.POST.get('title')
        text = request.POST.get('main_cont')

    return render(request, 'mark/task.html', {'form':TaskForm()})