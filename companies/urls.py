from django.urls import path

from companies import views

urlpatterns = [
    path("", views.CompanyCreateListView.as_view(), name="company_create_list"),
    path(
        "<int:pk>/",
        views.CompanyRetrieveUpdateDestroyView.as_view(),
        name="company_retrieve_update_destroy",
    ),
]
