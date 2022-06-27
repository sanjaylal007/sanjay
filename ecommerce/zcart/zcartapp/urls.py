from django.urls import path
from . import views


app_name='zcartapp'


urlpatterns = [
    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='all_products'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productdetail,name='product_category_detail')
]