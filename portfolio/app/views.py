# app/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'about.html', context=None)


class ContactPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'contact.html', context=None)