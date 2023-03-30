from django.urls import path

from home.controller import authview
from .import views
urlpatterns = [
    path('', views.index , name='home'),
    path('productall/', views.productall , name='productall'),
    path('productdetails/<int:id>', views.productdetails, name="productdetails"),  
    path('productcategory/<int:id>', views.categoryId, name="productcategory"), 
    path('search/', views.search , name='search'), 
    path('', views.category , name='home'),
    path('cart/', views.cart , name='cart'),


    path('regiser/', authview.registerr, name='regiser'),
    path('loginpage/', authview.loginpagee, name="loginpage"),
    path('logout/' , authview.logoutpagee, name="logout")
]
