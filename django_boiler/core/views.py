from django.shortcuts import render

def index(request, path):
    # , path
    return render(request, "index.html")
