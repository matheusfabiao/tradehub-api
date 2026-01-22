from django.urls import path

from sales import views

urlpatterns = [
    path("sales/", views.SaleCreateListView.as_view(), name="sale_create_list"),
    path(
        "sales/<int:pk>/",
        views.SaleRetrieveUpdateDestroyView.as_view(),
        name="sale_retrieve_update_destroy",
    ),
    path(
        "sales/stats/",
        views.SaleStatsView.as_view(),
        name="sale_stats",
    ),
]
