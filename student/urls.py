from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('home/',views.homePage,name="home"),
]
