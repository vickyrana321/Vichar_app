from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,DeleteView,UpdateView)

# Create your views here.
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)
