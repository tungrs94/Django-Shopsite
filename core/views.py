from django.shortcuts import render
from django.views import View
from product.models import Category, Product

# Create your views here.


class HomeView(View):
	def get(self, request):
		list_category = Category.objects.all()
		list_product = Product.objects.all()
		context = {'ds_cat': list_category, 'ds_product': list_product}
		return render(request, 'layout/index.html', context)


class BlogView(View):
	def get(self, request):
		return render(request, 'layout/blog.html')


# class CartView(View):
# 	def get(self, request):
# 		return render(request, 'layout/cart.html')


class ContactView(View):
	def get(self, request):
		return render(request, 'layout/contact.html')


class ProductView(View):
	def get(self, request):
		return render(request, 'layout/product.html')