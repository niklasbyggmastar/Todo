from django.shortcuts import render, redirect
from .models import Todo,Comment
from django.http import Http404

def index(request):
    recent_todoes = Todo.objects.all().order_by('-id')
    context = {'recent_todoes': recent_todoes,}
    return render(request, 'todo/index.html', context)

def detail(request, todo_id):
    #try:
    todo_text = Todo.objects.get(pk=todo_id)
    todoID = Todo.objects.get(pk=todo_id).id
    todoes = Todo.objects.all()
    index = 0
    for t in todoes:
        if (t.id != todoID):
            index += 1
        else:
            break

    if (todoes[index] == Todo.objects.all().last()):
        next_todo_id = todoes[index].id
    else:
        next_todo_id = todoes[index+1].id

    if (todoes[index] == Todo.objects.all().first()):
        prev_todo_id = todoes[index].id
    else:
        prev_todo_id = todoes[index-1].id

    todo_done = todo_text.todo_done
    recent_comments = todo_text.comment_set.all()
    if (recent_comments):
        todo_comment = Comment.objects.get(pk=todo_id)
    else:
        todo_comment = "No comments."
    context = {'todo_text': todo_text, 'todo_done': todo_done, 'todoID': todoID, 'todo_comment': todo_comment, 'next_todo_id':next_todo_id, 'prev_todo_id':prev_todo_id}
    #except:
        #raise Http404("Todo does not exist!")
    return render(request, 'todo/detail.html', context)

def new(request):
    if (request.method == 'POST'):
        text = request.POST['todo_text']
        todo = Todo(todo_text=text)
        todo.save()
        return redirect('/todo')
    else:
        return render(request, 'todo/new.html')

def update(request, todo_id):
    try:
        todoID = Todo.objects.get(pk=todo_id).id
        todo = Todo.objects.get(pk=todo_id)
        context = {'todo_text':todo, 'todoID':todoID}
        if (request.method == 'POST'):
            todo.todo_text = request.POST['todo_text']
            todo.save()

    except:
        raise Http404("Todo does not exist!")
    return render(request, 'todo/update.html', context)

#----------------------------------

def delete(request, todo_id):
    text = Todo.objects.get(pk=todo_id)
    text.delete()
    return redirect('/todo')

def toggle_done(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todoID = todo.id
    if (todo.todo_done == 1):
        todo.todo_done = 0
    elif (todo.todo_done == 0):
        todo.todo_done = 1
    todo.save()
    return redirect(request.META.get('HTTP_REFERER')) #redirect('/todo')

def comment(request, todo_id):
    todoID = Todo.objects.get(pk=todo_id).id
    todo = Todo.objects.get(pk=todoID)
    if (request.method == 'POST'):
        comment = todo.comment_set.create(todo_comment=request.POST['todo_comment'])
        comment.id = todoID
        comment.save()

    if (todo.todo_done == 1):
        todo.todo_done = 0
    elif (todo.todo_done == 0):
        todo.todo_done = 1
    todo.save()
    return redirect(request.META.get('HTTP_REFERER'))
