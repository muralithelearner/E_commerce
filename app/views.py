from django.shortcuts import render,redirect
from .models import Category,Product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.forms import UserCreateForm
# import uuid
from cart.cart import Cart


from django.contrib.auth import authenticate,login,logout   #for login authentication

# Create your views here.
@login_required(login_url='login')
def Master(request):
    return render(request,'master.html')

def index(request):
    category = Category.objects.all()
    category_ID = request.GET.get('category')
    if category_ID:
        product = Product.objects.filter(sub_category = category_ID).order_by('-id')
    else:
        product = Product.objects.all()

    #directory
    return render(request,'index.html',{'category': category,'product':product})

def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate (username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            return HttpResponse('Invalid user details')   
    else:
        return render(request,'loginpage.html')

def Logout(request):
    logout(request)
    return redirect(Login)

# def Reg_page(request):
#     return render(request,'regpage.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request,new_user)
            return redirect('logout')    
    else:
        form =UserCreateForm()
    return render(request,'registration/signup.html',{'form':form})


def Passowrd_rs_com(request):
    form = UserCreateForm()
    return render(request,'registration/password_reset_complete.html',{'form':form})

def Password_rs_con(request):
    form = UserCreateForm()
    return render(request,'registration/password_reset_confirm.html',{'form':form})

def Password_rs_don(request):
    return render(request,'registration/password_reset_done.html')

def Password_rs_form(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            return render(request,'registration/password_reset_don.html')
        else:
            # Form is not valid, return the form with errors
            return render(request, 'registration/password_reset_form.html', {'form': form})
    else:
        form = UserCreateForm() 
        return render(request,'registration/password_reset_form.html',{'form':form})


@login_required(login_url='login')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('index')

@login_required(login_url='login')
def item_clear(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect('index')

@login_required(login_url='login')
def item_increment(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request,'cart/cart_detail.html')

@login_required(login_url='login')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return render(request,'cart/cart_detail.html')

@login_required(login_url='login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url='login')
def cart_detail(request):
    return render(request,'cart/cart_detail.html')























# def Reg_page(request):
#     if request.method == 'GET':
#         form =RegistrationForm()
#         return render(request,'reg_page.html',{'form':form})
#     else:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(index)
#         else:
#             return HttpResponse("Plaease fill the all details")

     # views.py


# def Reg_page(request):
#     if request.method == 'GET':
#         form = RegistrationForm()
#         return render(request, 'reg_page.html', {'form': form})
#     elif request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = str(uuid.uuid4())[:30]  # Generate a unique username using UUID
#             user.set_password(form.cleaned_data['password'])  # Use 'password' instead of 'new_password'
#             user.save()
#             return redirect('index')  # Assuming 'index' is the name of your index view
#         else:
#             return render(request, 'reg_page.html', {'form': form})
#     else:
#         return HttpResponse("Invalid request method")


# def Reg_page(request):
#     if request.method == 'GET':
#         form = RegistrationForm()
#         return render(request, 'reg_page.html', {'form': form})
#     elif request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             # Use first_name and last_name to create a unique username
#             user.username = f"{form.cleaned_data['first_name']}_{form.cleaned_data['last_name']}"
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('index')  # Assuming 'index' is the name of your index view
#         else:
#             return render(request, 'reg_page.html', {'form': form})
#     else:
#         return HttpResponse("Invalid request method")

