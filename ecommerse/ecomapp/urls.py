from . import views
from django.urls import path

app_name = 'ecomapp'
urlpatterns = [

    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.proDetail, name='prodCatDetails'),
]
