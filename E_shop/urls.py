"""
URL configuration for E_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings  # for image display from backend
from django.conf.urls.static import static   # for image display from backend
from app import views 

app_name = 'cart'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master',views.Master,name='master'),
    path('',views.index,name='index'),
    path('login',views.Login,name='login'),
    path('signup',views.signup,name='signup'),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('logout',views.Logout,name='logout') ,

    path('password_rs_com',views.Passowrd_rs_com, name='password_rs_com'),
    path('password_rs_con',views.Password_rs_con, name='password_rs_con'),
    path('password_rs_don',views.Password_rs_don, name='password_rs_don'),
    path('password_rs_form', views.Password_rs_form, name='password_rs_form'),

    #cart
    path('cart/add<int:id>',views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/',views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear',views.cart_clear, name='cart_clear'),
    path('cart/cart_detail',views.cart_detail, name='cart_detail')



    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)   # for image display from backend

