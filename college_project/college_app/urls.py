from django.urls import path
from . import views

app_name = 'college_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('student_form', views.student_form, name='student_form'),
    path('login/', views.login, name='login'),
    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout, name='logout')
]