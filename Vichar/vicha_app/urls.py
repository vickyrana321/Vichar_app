
# from django.contrib import admin
# from django.urls import path
# from django.urls.resolvers import URLPattern
# from . import views
# from django.views.generic import (View,TemplateView,ListView,DetailView,
#                                   CreateView,DeleteView,UpdateView)
# urlpatterns=[
#      path('',views.HomePage.as_view(),name='home'),
#  ]
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'vicha_app'

urlpatterns = [
    url(r"login/$", auth_views.LoginView.as_view(template_name="vicha_app/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
]