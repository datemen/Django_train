'''
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import 
from .forms import 
from django.views.generic import CreateView, TemplateView
'''
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate ,logout
from accounts.models import User
from django.views.generic import CreateView, TemplateView
from . forms import CreateForm , LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(TemplateView):
    template_name = 'accounts/index.html'
index = Index.as_view()

class Create_Accounts(CreateView):
    def post(self, request, *args, **kwargs):
        form = CreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            #フォームに入力された'username', 'password1'が一致する会員をDBから探し，userに代入
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/sns')
        return render(request, 'accounts/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = CreateForm(request.POST)
        return  render(request, 'accounts/create.html', {'form': form,})

create_account = Create_Accounts.as_view()

#ログイン
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/sns')
        return render(request, 'accounts/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'accounts/login.html', {'form': form,})

account_login = Account_login.as_view()

#ログアウト
class Account_logout(LoginRequiredMixin, TemplateView):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('/accounts')
account_logout = Account_logout.as_view()