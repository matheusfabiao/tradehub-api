from django.urls import path

from customers import views

urlpatterns = [
    path("", views.CustomerCreateListView.as_view(), name="customer_create_list"),
    path(
        "<int:pk>/",
        views.CustomerRetrieveUpdateDestroyView.as_view(),
        name="customer_retrieve_update_destroy",
    ),
]
