"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
import django
from django.contrib.auth import views as django_auth_views # django内部认证
app_name = 'account'  # 增加app_name变量呼应 include中的namespace
urlpatterns = [
    # re_path('^login/$', views.user_login, name="user_login"),
    # path('login/', django_auth_views.LoginView.as_view(), name="user_login"), # 另一种写法如下
    path('login/', django_auth_views.LoginView.as_view(), {"template_name": "account/login.html"}, name="user_login"),
    # path('logout/', django_auth_views.LogoutView.as_view(), name="user_logout"),
    path('logout/', django_auth_views.LogoutView.as_view(), {"template_name": "account/logged_out.html"}, name="user_logout"),
    re_path('^register/$', views.register, name="user_register"),
    re_path('^password-change/$', django_auth_views.PasswordChangeView.as_view(), name='password_change'),
    re_path('^password-change-done/$', django_auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    re_path('^password-reset/$', django_auth_views.PasswordResetView.as_view(),
            {"template_name": "account/password_reset_form.html",
             "email_template_name": "account/password_reset_email.html",
             "subject_template_name": "account/password_reset_subject.txt",
             "post_reset_redirect": "/account/password-reset-done"},
            name='password_reset'),

    re_path('^password-reset-done/$', django_auth_views.PasswordResetDoneView.as_view(),
            {"template_name":"account/password_reset_done.html"},
            name='password_reset_done'),

    re_path('^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            django_auth_views.PasswordResetConfirmView.as_view(),
            {"template_name": "account/password_reset_confirm.html",
             "post_reset_redirect": "/account/password-reset-complete"},
            name="password_reset_confirm"),

    re_path('^password-reset-complete/$', django_auth_views.PasswordResetCompleteView.as_view(),
            {"template_name": "account/password_reset_complete.html"},
            name="password_reset_complete"),
]