from django.shortcuts import render
import json
from django.http import Http404, HttpResponse
from app.models import Todo
from app.forms import TodoForm
# Create your views here.
def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.is_ajax() and request.POST:
        text = request.POST.get('comment')
        todo = Todo(text=text)
        todo.save()
        data = {'message': request.POST.get('comment')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'app/index.html',{'todos': todos, 'form': form})
