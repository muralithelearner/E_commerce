from django.contrib import admin

# Register your models here.
from . models import Category,Sub_Category,Product
#Registrationpage

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
# admin.site.register(Registrationpage)
