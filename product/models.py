from django.db import models

# Create your models here.


class Category(models.Model):
	title 		= models.CharField(default = '', max_length = 255)
	slug 		= models.CharField(default = '', max_length = 100)
	description = models.TextField(default = '')
	active 		= models.BooleanField(default = True)

	def __str__(self):
		return self.title


class Product(models.Model):
	title 		= models.CharField(default = '', max_length = 255)
	description = models.TextField(default = '')
	category 	= models.ForeignKey(Category, on_delete = models.CASCADE)
	product_img = models.CharField(default = '', max_length = 255)
	price 		= models.IntegerField(default = 0)
	active 		= models.BooleanField(default = True)

	def __str__(self):
		return self.title


class Variation(models.Model):
	product 	= models.ForeignKey(Product, on_delete = models.CASCADE)
	title 		= models.CharField(default = '', max_length = 255)
	price 		= models.IntegerField(default = 0)
	sale_price 	= models.IntegerField(default = 0)
	inventory 	= models.IntegerField(default = 0)
	active 		= models.BooleanField(default = True)

	def __str__(self):
		return self.title