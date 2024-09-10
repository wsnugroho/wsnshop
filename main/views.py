from django.shortcuts import render


def show_main(request):
    context = {
        "npm": 2306275084,
        "name": "Wisnu Nugroho",
        "class": "PBP D",
    }
    return render(request, "main.html", context)
