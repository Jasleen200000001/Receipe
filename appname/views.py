from django.shortcuts import render
from django.http import HttpResponse
from .models import Clas

from .form import Pythonform


def myform(request):
    if request.method == 'POST':
        data = Pythonform(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            age = data.cleaned_data['age']
            return render(request, template_name='form.html', context={'name': name})
        else:
            data = Pythonform()
            return render(request, template_name='form.html', context={'data': data})


def read(request):
    classes = Clas.objects.all()
    return render(request, template_name='webpages/index.html', context={'classes': classes})
