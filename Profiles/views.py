from django.shortcuts import render
from django.http import HttpResponseRedirect
from Profiles.models import HomeBanner
from Products.models import SampleProducts, Products, UserCartProducts


def user_register(request):
    return render(
                  request,
                  'profiles/register.html',
                  {}
                 )


def user_home(request):
    home_banner = HomeBanner.objects.filter(active=True).order_by('order')
    home_about = SampleProducts.objects.filter(active=True).order_by('order')
    home_products = Products.objects.filter(active=True).order_by('?')
    try:
        cart_item = UserCartProducts.objects.get(user=request.user)
    except Exception:
        cart_item = None
    return render(
                  request,
                  'profiles/index.html',
                  {
                      'home_banner': home_banner,
                      'home_about': home_about,
                      'home_products': home_products,
                      'cart_item': cart_item
                  }
                 )


def add_cart_item(request):
    item_id = request.GET.get('item')
    if item_id:
        try:
            products = Products.objects.get(pk=int(item_id))
            user_cart_items, created = \
                UserCartProducts.objects.get_or_create(user=request.user)
            if user_cart_items:
                user_cart_items.products.add(products)
        except Exception:
            products = None
    return HttpResponseRedirect('/home/')


def empty_cart_items(request):
    cart_item = UserCartProducts.objects.get(user=request.user)
    cart_item.products.clear()
    return HttpResponseRedirect('/home/')


def veg_blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})
