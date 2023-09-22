
from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name='test'),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.signuppage, name='signup'),
    path('home/',views.homepage, name='homepage'),
    path('uploadimage/', views.upload_image, name='upload_image'),
]