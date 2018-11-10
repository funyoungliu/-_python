"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name='users'
LoginView.template_name = 'users/login.html'
urlpatterns=[
    #登录页面
    url('login/',LoginView.as_view(),name='login'),
    #注销
    url('logout',views.logout_view,name='logout'),
    #注册页面
    url('register/',views.register,name='register'),
]