from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
     path('', views.home, name="home"),
     path('contact', views.contact, name="contact"),
     path('about', views.about, name="about"),
     path('FAQ', views.faq, name="faq"),
     path('list', views.product_list, name="product_list"),
     path('special_offers', views.special_offers, name="special_offer"),
     path('<slug:category_slug>/', views.product_list,
          name='product_list_by_category'),
     path('<int:id>/<slug:slug>/', views.product_detail,
          name='product_detail'),
]
