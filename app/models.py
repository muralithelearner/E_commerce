from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):    # without use this function actuval names not display in database
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):    # without use this function actuval names not display in database
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,default='')  #null= true( u can add without menssion category)
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=True,default='')
    image = models.ImageField(upload_to='ecomers/pimg')  # add image feild in db should be install pillow
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


















# class Registrationpage(models.Model):
#     first_name =models.CharField(max_length=25)
#     surname =models.CharField(max_length=25)
#     contactinput = models.CharField(max_length=100, validators=[validate_email, RegexValidator(regex='^[0-9]{10}$', message='Enter a valid 10-digit mobile number.')])
#     contactinput = models.BigIntegerField()
#     new_password = models.CharField(max_length=25)
#     date_feild =models.DateField()
#     gender =models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.first_name} {self.surname}"



    



