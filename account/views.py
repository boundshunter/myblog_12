from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
# authenticate, login 内置方法，用户认证和管理应用


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('Welcome, You have been authenticated successfully')
            else:
                return HttpResponse('Sorry, Your username or password is invalid!')
        else:
            return HttpResponse('Invalid Login ')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'account/login.html', {"form": login_form})