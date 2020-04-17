from django.shortcuts import render
from django.views import View
from .models import Category

# Create your views here.

# class CategoryView(View):
# 	def get(self, request):
# 		list_category = Category.objects.all()
# 		context = {'ds_cate': list_category}
# 		return render(request, context)