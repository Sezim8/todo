from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book


def homepage(request):
    return render(request, "index.html")\

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})
# Эта задание к 32-уроку


def third(request):
    return HttpResponse("This is page test3")

def fourth(request):
    return render(request, "31.1.html")

def fifth (request):
    return render(request, "31.2.html")
def sixth (request):
    return render(request, "31.3.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})

def add_todo (request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()

    return redirect (test)


def add_book(request):
    form = request.POST
    todo = Book(
        title=form['title'],
        subtitle=form['subtitle'],
        year=form['year'] [:10],
        desciption=form['desciption'],
        author=form['author'],
        price=form['price'],
    )
    todo.save()
    return redirect (books)
    
def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect (test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect (test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect (test)
   



   
