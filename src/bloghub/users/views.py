from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.urls import reverse

from posts.models import Author
from main.functions import generate_form_errors

from .forms import UserForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            print("entered user")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                
                return HttpResponseRedirect('/')

        context = {
            'title': 'Login',
            'error': True,
            'message': "Invalid username or password"
        }
        return render(request, 'users/login.html', context)
    else:
        context = {
                    'title': 'Login',
                }
    return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def signup(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user.set_password(password)
            # user.save()

            User.objects.create_user(
                username = user.username,
                password = user.password,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )
            
            user.save()  # Save the user object
            
            Author.objects.create(name=user.username, user=user) # creates author when we reigister

            user = authenticate(username=user.username, password=user.password)

            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('web:index'))
        else:
            message = generate_form_errors(form)

            form = UserForm()
            context = {
                'title': 'Signup',
                'form': form,
                'message': message
            }
            print(context)
    else:
        form = UserForm()

        context = {
            'title': 'Signup',
            'form': form
        }
    return render(request, 'users/signup.html', context)