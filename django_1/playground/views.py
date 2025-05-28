from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

# Create your views here.
# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Django Student'})

def show_form(request):
    submitted_name = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            submitted_name = form.cleaned_data['your_name']
    else:
        form = NameForm()
    return render(request, 'form.html', {'form': form, 'submitted_name': submitted_name})