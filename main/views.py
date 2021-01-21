from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")
def test(request):
    return render(request, "test.html")

def third(request):
    return HttpResponse("This is page test3")

def fourth(request):
    return render(request, "31.1.html")

def fifth (request):
    return render(request, "31.2.html")
def sixth (request):
    return render(request, "31.3.html")

