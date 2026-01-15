from django.urls import path

from sales import views

urlpatterns = [
    path("", views.SaleCreateListView.as_view(), name="sale_create_list"),
    path(
        "<int:pk>/",
        views.SaleRetrieveUpdateDestroyView.as_view(),
        name="sale_retrieve_update_destroy",
    ),
]
