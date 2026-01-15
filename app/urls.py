from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("companies/", include("companies.urls")),
    path("customers/", include("customers.urls")),
    path("products/", include("products.urls")),
    path("sales/", include("sales.urls")),
]
