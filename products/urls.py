from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductCreateListView.as_view(), name="product_create_list"),
    path(
        "<int:pk>/",
        views.ProductRetrieveUpdateDestroyView.as_view(),
        name="product_retrieve_update_destroy",
    ),
]
