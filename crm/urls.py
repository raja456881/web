from django.urls import path
from.import views
urlpatterns = [
    path('/user',views.user,name='user'),
    path("/raja" ,views.BulckEmail, name='bulkemail'),
    path('/singlemail', views.studentsingeemail, name='singlemail'),
    path('/singlemail1', views.Institutionsingeemail),
    path('/single2', views.trainersingeemail),
    path('/location', views.location, name='location'),
    path('/hello', views.HelloPDFView.as_view()),
    path('/<int:pk>/', views.pdf_view),


]
