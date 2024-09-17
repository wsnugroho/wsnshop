from django.urls import path

from main.views import (create_product, show_json, show_json_by_id, show_main,
                        show_xml, show_xml_by_id)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product", create_product, name="create_product"),
    path("xml", show_xml, name="show_xml"),
    path("xml/<str:id>", show_xml_by_id, name="show_xml_by_id"),
    path("json", show_json, name="show_json"),
    path("json/<str:id>", show_json_by_id, name="show_json_by_id"),
]
