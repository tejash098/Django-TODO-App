from django.shortcuts import render
from .models import Todo
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'todolist/index.html')

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/home.html', {'todos': todos})

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todolist/home.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Status = request.POST.get('status')
        print(title, due_date, Status)
        user = request.user
        Todo.objects.create(title=title, due_date=due_date, Status=Status, user=user)
        return redirect('todo_list')
    return render(request, 'todolist/home.html')

def todo_update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Status = request.POST.get('Status')
        user = request.user
        Todo.objects.update(title=title, due_date=due_date, Status=Status, user=user)
        return redirect('todo_list')
    return render(request, 'todolist/home.html', {'todo': todo})

def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
