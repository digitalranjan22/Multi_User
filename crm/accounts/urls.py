from django.urls import path
from . import views



urlpatterns = [
    path('register/',views.registerPage),
    path('login/',views.loginPage),
    # path('login/home',views.home),
    path('logout/',views.logoutUser),




    path('',views.home),
    path('user/',views.userPage ,name='user-page'),
    path('products/',views.product),
    path('customers/',views.customer),
   
]