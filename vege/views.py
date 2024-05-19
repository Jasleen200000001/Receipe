from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


@login_required(login_url="login_page")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('receipes')

    read = Receipe.objects.all()

    if request.GET.get('search_re'):
        read = read.filter(receipe_name__icontains = request.GET.get('search_re'))

    return render(request,template_name='receipes.html',context={'receipes': read })

# def delete_receipe(request, id):
#     findId = Receipe.objects.get(id=id)
#     receipe_image = request.FILES.get('receipe_image')
#
#     findId.delete()
#
#     return redirect('receipes')

def delete_receipe(request, id):
    # Use get_object_or_404 to safely retrieve the recipe object
    recipe = get_object_or_404(Receipe, id=id)

    # Delete the image file from the file system
    # This step is crucial to prevent orphaned files
    if recipe.receipe_image:
        recipe.receipe_image.delete()

    # Finally, delete the recipe object
    recipe.delete()

    return redirect('receipes')

def update_receipe(request,id):
    findId= Receipe.objects.get(id=id)
    return render(request,template_name='updateReceipes.html',context={'r': findId })

def update_link(request,id):
    findId = Receipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        if receipe_name:
            findId.receipe_name = receipe_name
        if receipe_description:
            findId.receipe_description = receipe_description
        if receipe_image:
            findId.receipe_image = receipe_image

        findId.save()
    return redirect("receipes")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "invalid username")
            return redirect('/login-page')

        user = authenticate(username=username , password = password)

        if user is None:
            messages.error(request, "invalid password")
            return redirect('/login-page')
        else:
            login(request, user)
            return redirect('receipes')

    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "user name already exists ")
            return redirect('/register-page')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "account created success fully")
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('login-page')
