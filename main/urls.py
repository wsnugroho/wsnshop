from django.urls import path

from main.views import create_product, show_main

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product", create_product, name="create_product"),
]
