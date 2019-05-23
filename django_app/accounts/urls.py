from django.urls import path
from . import views


urlpatterns = [
        path('',views.index,name='index'),
        path('create/',views.create_account,name='create_account'),
        path('login/',views.account_login,name='login'),
        path('logout/', views.account_logout, name='logout'),
        ]

