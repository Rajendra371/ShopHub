from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
   
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=100, default="")
    price=models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")
   

    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    




# class Order(models.Model):
#     PAYMENT = (
#         ('Cash on Delivery','Cash on Delivery'),
#         ('Esewa','Esewa')
#     )

#     product=models.ForeignKey(Orders,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity=models.IntegerField()
#     total_price=models.IntegerField()
#     deliver_status=models.CharField(default='Pending',max_length=255)
#     payment_method=models.CharField(max_length=255,choices=PAYMENT)
#     payment_status=models.BooleanField(default=False,null=True,blank=True)
#     contact_no=models.CharField(max_length=15)
#     address=models.CharField(max_length=100,null=True)
#     created_at=models.DateTimeField(auto_now_add=True,null=True)
    

    
