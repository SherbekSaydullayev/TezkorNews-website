from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import *
import requests

# class HomePageView(DetailView):
# 	model = Xabar
# 	template_name = 'post_detail.html'


def indexPageView(request):
	yangilik = News.objects.all()
	context = {
	"yangiliklar":yangilik,
	}
	return render(request,'index.html',context)



def homePageView(request,news_id):
	malumot = News.objects.filter(id=news_id)
	yangilik2 = malumot[0]
	context = {
	"yangiliklar2": yangilik2
	}
	return render(request,'post_detail.html',context)


# class CategoryPageView(ListView):
# 	model = Xabar
# 	template_name = 'category.html'

def categoryPageView(request,category_id):
	category_uchun2 = Category.objects.get(pk=category_id)
	yangilik3 = News.objects.filter(category_id=category_uchun2)
	context = {
	"category_uchun": category_uchun2,
	"yangiliklar3": yangilik3
	}
	return render(request,'category.html',context)