from django.shortcuts import render
from django.http import HttpResponse

def get_homepage(request):
    context = {
        "coins": Crypto.objects.all()
    }
    return render(
        request, "main/homepage.html", context
        )