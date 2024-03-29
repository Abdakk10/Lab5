# myapp/views.py
from django.shortcuts import render

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []  # List to store Person objects

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)

    return render(request, 'myapp/add.html')

def show_all(request):
    return render(request, 'myapp/show_all.html', {'people': people})
