from django.db import models
from django.db.models import Q
class Product(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name

class Side(models.Model):
    name =models.CharField( max_length=50)
    type = models.CharField( max_length=50)
    def __str__(self):
        return self.name

    def get_in(self,product_id=None):
        if product_id:
            product =Product.objects.get(id=product_id)
            move_in = Movment.objects.filter(reciver =self).filter(product=product)
            return move_in
        else:
            move_in = Movment.objects.filter(reciver =self)
            return move_in

    def get_out(self,product_id=None):
        if product_id:
            product =Product.objects.get(id=product_id)
            move_out = Movment.objects.filter(sender =self).filter(product=product)
            return move_out
        else:
            move_out = Movment.objects.filter(sender =self)
            return move_out

class ProductDetail (models.Model):
    product =models.ForeignKey("Product",related_name="detail", on_delete=models.CASCADE) 
    place  = models.ForeignKey("Side", related_name="detail", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

class Movment (models.Model):
    product=models.ForeignKey("Product", on_delete=models.CASCADE)
    amount =models.PositiveIntegerField()
    sender = models.ForeignKey("Side", related_name='send', on_delete=models.CASCADE)
    reciver= models.ForeignKey("Side", related_name='recive', on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.product}  from {self.sender}  to {self.reciver}"
        