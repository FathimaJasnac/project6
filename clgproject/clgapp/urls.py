from django.urls import path
from . import views
app_name='clgapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('student_form/', views.student_form, name='student_form')
    # path('success_message/', views.student_form, name='student_form')

]
