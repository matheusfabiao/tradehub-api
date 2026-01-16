from django.urls import path

from companies import views

urlpatterns = [
    path(
        "companies/", views.CompanyCreateListView.as_view(), name="company_create_list"
    ),
    path(
        "companies/<int:pk>/",
        views.CompanyRetrieveUpdateDestroyView.as_view(),
        name="company_retrieve_update_destroy",
    ),
]
