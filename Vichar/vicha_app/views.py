from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
#when someone is logged in or logged out where should they go thats why use reverse lazy
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,DeleteView,UpdateView)
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")#once user succefully signup the form he is redirected/reversed 
    #login page
    template_name = "vicha_app/signup.html"