from django.urls import path
from basicApp import views

#template variables
app_name='basicApp'

urlpatterns=[
        path('register/',views.register,name='register'),
        path('userlogin/',views.user_login,name='user_login'),
]
