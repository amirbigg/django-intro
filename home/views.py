from django.shortcuts import render
from .models import Todo



def home(request):
	all = Todo.objects.all()
	return render(request, 'home.html', {'todos':all})


def say_hello(request):
	return render(request, 'hello.html', {'name':'jack'})
