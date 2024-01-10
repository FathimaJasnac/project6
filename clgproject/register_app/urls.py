from django.urls import path
from . import views
app_name='register_app'

urlpatterns = [

   path('login/',views.login,name='login'),
   path('reg/',views.reg,name='reg'),
   path('logout/',views.logout,name='logout')
]