from django.shortcuts import render

def index(request):
    return render(request,"primo_progetto/index_root.html")