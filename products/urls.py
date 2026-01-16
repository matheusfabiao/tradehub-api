from django.urls import path

from products import views

urlpatterns = [
    path(
        "products/", views.ProductCreateListView.as_view(), name="product_create_list"
    ),
    path(
        "products/<int:pk>/",
        views.ProductRetrieveUpdateDestroyView.as_view(),
        name="product_retrieve_update_destroy",
    ),
]
