from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100, default='buyer')

    def __str__(self):
        return self.username + ' ' + self.usertype

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_products')
    product_name = models.CharField(max_length=100)
    product_price = models.PositiveIntegerField()
    product_pic = models.ImageField(upload_to="product_pic/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    

class Whishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField()
    product_qty = models.PositiveIntegerField()
    totol_price = models.PositiveIntegerField()
    payment_status = models.BooleanField(default=False)


