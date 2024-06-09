
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),


    # urls.py
    path('edit-details/<int:pk>/', views.edit_details, name='edit-details'),
    path('logout_profile/',views.logout_profile,name='logout_profile'),
    path('add_product',views.add_product,name='add_product'),
    path('seller_index',views.seller_index,name='seller_index'),
    path('vegetables/<str:foo>',views.vegetables,name='vegetables'),
    path('Fruits/<str:foo>',views.Fruits,name='Fruits'),
    path('Bread/<str:foo>',views.Bread,name='Bread'),
    path('Meat/<str:foo>',views.Meat,name='Meat'),
    path('all_products',views.all_products,name='all_products'),
    path('product_detail/<int:pk>/',views.product_detail,name='product_detail'),
    path('edit_product/<int:pk>/',views.edit_product,name='edit_product'),
    path('buyer_product_detail/<int:pk>',views.buyer_product_detail,name='buyer_product_detail'),
    path('add_to_whishlist/<int:pk>',views.add_to_whishlist,name='add_to_whishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('remove_wishlist/<int:pk>',views.remove_wishlist,name='remove_wishlist'),

    # url for a wishlist page 
    path('wishlist_remove/<int:pk>',views.wishlist_remove,name='wishlist_remove'),
    path('addcart/<int:pk>/',views.addcart,name='addcart'),
    path('cart/',views.cart,name='cart'),
    path('change-qty/',views.change_qty,name='change-qty')


    
    
    
    


]
