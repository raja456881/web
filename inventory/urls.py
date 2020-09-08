from django.urls import path
from . import views
urlpatterns = [
    path('inventory',views.inventory, name = 'inventory'),
    path('edit/<int:pk>/',views.editCourse, name = 'editCourse'),
    path('fillcourse',views.fillcourse,name='fillcourse'),
    path('', views.course, name='course')
]