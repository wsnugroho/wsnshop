from django.core import serializers
from django.shortcuts import HttpResponse, redirect, render

from main.forms import ProductForm
from main.models import Product


def show_main(request):
    products = Product.objects.all()
    context = {
        "npm": 2306275084,
        "name": "Wisnu Nugroho",
        "class": "PBP D",
        "products": products,
    }
    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    context = {"form": form}
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )
