import datetime
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from main.functions import generate_form_errors, pagination
from main.decorators import allow_self
from posts.models import Author, Category, Post
from posts.forms import PostForm


@login_required(login_url='/users/login')
def create_post(request):

    if not request.method == 'POST':
        form = PostForm()

        context = {
            "title": 'Create New Post',
            'page_id': 'edit-post-home',
            'form': form,
        }

        print("template loaded")
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # for image files

        if form.is_valid():

            tags = form.cleaned_data['tags']

            if not Author.objects.filter(user=request.user).exists():
            
                author = Author.objects.create(user=request.user, name=request.username)
            else:
                author = request.user.author

            instance = form.save(commit=False)
            instance.published_date = datetime.date.today()
            instance.author = author
            instance.save()

            tags_list = tags.split(",")
            for tag in tags_list:
                category, created = Category.objects.get_or_create(title=tag.strip())
                instance.categories.add(category)
            
            response_data = {
                "message": "Your new post has been created successfully",
                "title": "Successfully Created",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/"
            }

        else:
            error_message = generate_form_errors(form)
            print(error_message)
            response_data = {
                "message": str(error_message),
                "title": "Oops",
                "status": "error",
                "stable": "yes"
            }
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
    return render(request, 'posts/create.html', context)


@login_required(login_url='/users/login')
def my_posts(request):

    posts = Post.objects.filter(author=request.user.author, is_deleted=False)

    paginator_instance = pagination(request, posts, 6)

    context = {
        "title": "My Posts",
        "page_id": "my-posts-home",
        "paginator_instance": paginator_instance
    }

    return render(request, 'posts/my-posts.html', context)


@login_required(login_url='/users/login')
@allow_self
def delete_post(request, pk):

    post = get_object_or_404(Post, id=pk)

    post.is_deleted = True
    post.save()
    
    response_data = {
        "message": "Your Post has been deleted successfully",
        "title": "Deleted Successfully",
        "status": "success",
        "redirect": "not",
        "redirect_url": "",
        "stable": "no",
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    

@login_required(login_url='/users/login')
@allow_self
def draft_or_publish(request, pk):

    post = get_object_or_404(Post, id=pk)
    if post.is_draft:
        post.is_draft = False
        post.save()
        
        response_data = {
            "message": "Your Post has been uploaded successfully",
            "title": "Uploaded Successfully",
            "status": "success",
            "redirect": "not",
            "redirect_url": "",
            "stable": "no",
        }
    else:
        post.is_draft = True
        post.save()
        
        response_data = {
            "message": "Your Post has been saved as a draft successfully",
            "title": "Draft Saved Successfully",
            "status": "success",
            "redirect": "not",
            "redirect_url": "",
            "stable": "no",
        }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    

@login_required(login_url='/users/login')
@allow_self
def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if not request.method == 'POST':
        categories_string = ""
        for category in post.categories.all():
            categories_string += category.title + ", "
        form = PostForm(instance=post, initial={'tags': categories_string[:-1]})

        context = {
            "title": 'Edit Post',
            'page_id': 'edit-post-home',
            'form': form,
        }

        print("template loaded")
            
        return render(request, 'posts/create.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) # for image files

        if form.is_valid():

            tags = form.cleaned_data['tags']

            instance = form.save(commit=False)
            instance.save()

            instance.categories.clear()  

            tags_list = tags.split(',')
            
            for tag in tags_list:
                category, created = Category.objects.get_or_create(title=tag.strip())
                instance.categories.add(category)

            response_data = {
                "message": "Your new post has been edited successfully",
                "title": "Successfully Edited",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/"
            }

        else:
            error_message = generate_form_errors(form)
            print(error_message)
            response_data = {
                "message": str(error_message),
                "title": "Oops",
                "status": "error",
                "stable": "yes"
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


