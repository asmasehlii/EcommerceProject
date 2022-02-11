from django.urls import path
from . import views

urlpatterns = [

    path("product-list/", views.ListProductAPIView.as_view(), name="product_list"),
    path("create-product/", views.CreateProductAPIView.as_view(), name="product_create"),
    path("update-product/<int:pk>", views.UpdateProductAPIView.as_view(), name="product_update"),
    path("delete-product/<int:pk>", views.DeleteProductAPIView.as_view(), name="product_delete"),
    path("details-product/<int:pk>", views.DetailProductAPIView.as_view(), name="product_detail"),
    ]
