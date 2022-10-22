from datetime import datetime
from email.policy import default
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=15)
    country_id = models.ForeignKey(Country, on_delete=CASCADE)
    def __str__(self) -> str:
        return self.state_name

class City(models.Model):
    city_name = models.CharField(max_length=15)
    state_id = models.ForeignKey(State, on_delete=CASCADE)
    def __str__(self) -> str:
        return self.city_name

    
class UserBase(models.Model):
    user_id=models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    first_name=models.CharField(max_length=45,null=True,blank=True)
    last_name=models.CharField(max_length=45,null=True,blank=True)
   
    cus_add1=models.TextField(null=True,blank=True,default=" ")
    cus_add2=models.TextField(null=True,blank=True,default=" ")
    pincode=models.IntegerField(null=True,blank=True,default=0)
    cus_phone=models.CharField(max_length=10,null=True,blank=True,default=" ")
    wp=models.CharField(max_length=10,null=True,blank=True,default=" ")
    profile=models.ImageField(upload_to="profileImages/",max_length=1500,null=True,blank=True)
    city_id=models.ForeignKey(City,on_delete=CASCADE,null=True,blank=True)
    aboutme=models.CharField(max_length=1500,null=True,blank=True,default=" ")

    website=models.URLField(null=True,blank=True,default=" ")
    bank_details=models.CharField(max_length=1500,null=True,blank=True,default=" ")
    paymentQR=models.ImageField(upload_to="ORs/",max_length=255,null=True,blank=True,default=" ")
    visitor_count=models.IntegerField(null=True,blank=True,default=0)
    skype=models.URLField(null=True,blank=True,default=" ")
    organization=models.CharField(max_length=255,null=True,blank=True,default=" ")
    designation=models.CharField(max_length=255,null=True,blank=True,default=" ")
    fb=models.URLField(null=True,blank=True,default=" ")
    twitter=models.URLField(null=True,blank=True,default=" ")
    linkedin=models.URLField(null=True,blank=True,default=" ")
    ig=models.URLField(null=True,blank=True,default=" ")
    yt=models.URLField(null=True,blank=True,default=" ")
    gps=models.URLField(null=True,blank=True,default=" ",max_length=500)
    class meta:
        ordering = ['user_id']
    def __str__(self) -> str:
        return self.user_id.username

class Product(models.Model):
    product_name=models.CharField(max_length=45,null=True,blank=True)
    status=models.CharField(max_length=30,default="active")
    desc=models.TextField(null=True,blank=True)
    product_img=models.ImageField(upload_to="ProductImg/",max_length=100,null=True,blank=True)
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE)
    def __str__(self) -> str:
        return self.product_name

class Complaint(models.Model):
    title=models.CharField(max_length=45,null=True,blank=True)
    com_desc=models.CharField(max_length=200,null=True,blank=True)
    com_date=models.DateField(auto_now=True,null=True,blank=True)
    client_mail=models.CharField(max_length=250,null=True,blank=True)
    userbase=models.ForeignKey(UserBase,on_delete=CASCADE)
    def __str__(self):
        return self.title


class Appointment(models.Model):
    app_date=models.DateField()
    app_status=models.IntegerField(default=0)
    app_time=models.TimeField()
    app_title=models.CharField(max_length=30)
    client_email=models.CharField(max_length=50,default=None)
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE,default=None)
    def __str__(self) -> str:
        return str(self.id)


class Testimonial(models.Model):
    client_name=models.CharField(max_length=20)
    client_image=models.ImageField(upload_to='Testimonials/')
    test_title=models.CharField(max_length=45)
    test_desc=models.TextField()
    test_date=models.DateTimeField(auto_now=True)
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE,default=None)
    
    def __str__(self) -> str:
        return self.test_title

class Gallery(models.Model):
    gallery_img=models.ImageField(upload_to="Gallery/")
    gallery_name=models.CharField(max_length=20)
    status=models.CharField(max_length=15,default="Active")
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE)
    def __str__(self) -> str:
        return str(self.id)

class Vgallery(models.Model):
    vgallery_name=models.CharField(max_length=20)
    vgallery_link=models.CharField(max_length=250)
    status=models.CharField(max_length=15,default="Active")
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE)
    def __str__(self) -> str:
        return str(self.id)

class Service(models.Model):
    service_img=models.ImageField(upload_to="ServiceImg/",max_length=100)
    service_name =models.CharField(max_length=70)
    service_desc=models.CharField(max_length=70)
    status=models.CharField(max_length=30,default="active")
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE)
    def __str__(self) -> str:
        return str(self.service_name)
        
class Package(models.Model):
    package_name=models.CharField(max_length=70)
    package_price=models.IntegerField()
    features=models.JSONField(default="{'demo':'demo'}")

class Mypackage(models.Model):
    package_expire_date=models.DateField()
    status=models.CharField(max_length=30,default="active")
    user_id=models.ForeignKey(UserBase,on_delete=CASCADE)
    package_id=models.ForeignKey(Package,on_delete=CASCADE)
    # transaction,package 
    def __str__(self) -> str:
        return str(self.package_name)




# class Transaction(models.Model):
#     made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
#     made_on = models.DateTimeField(auto_now_add=True)
#     amount = models.IntegerField()
#     order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
#     checksum = models.CharField(max_length=100, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if self.order_id is None and self.made_on and self.id:
#             self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
#         return super().save(*args, **kwargs)