from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(

    'Profiles.views',

    url(
        r'^register/$',
        'user_register',
        name='user-register'
        ),

    url(
        r'home/$',
        'user_home',
        name='user-home'
        ),

    url(
        r'^add-cart-item/$',
        'add_cart_item',
        name='add-cart-item'
        ),

    url(
        r'^empty-cart/$',
        'empty_cart_items',
        name='empty-cart-item'
        ),

    url(
        r'^blog/$',
        'veg_blog',
        name='veg-blog'
        ),

    url(
        r'^contact/$',
        'contact',
        name='contacts'
        ),

)
