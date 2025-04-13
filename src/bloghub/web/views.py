from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from main.functions import pagination

from posts.models import Author, Category, Post
from users.views import login



@login_required(login_url='users/login')
def index(request):
    posts = Post.objects.filter(is_draft=False, is_deleted=False)

    categories = Category.objects.all()
    authors = Author.objects.all()

    search = request.GET.get("q")

    if search:
        # posts = posts.filter(title__search=search)
        # posts = posts.annotate(search=SearchVector('title', 'author__name', 'categories__title')).filter(search=search)

        """
        vector = SearchVector('title', 'author__name', 'categories__title')
        query = SearchQuery(search)
        posts = Post.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')

        """
        vector = SearchVector('title', weight='A') + SearchVector('author__name',  weight='B') + SearchVector('categories__title',  weight='C')
        query = SearchQuery(search)
        posts = Post.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')

        print(posts)

    authors_query = request.GET.getlist("author")
    categories_query = request.GET.getlist("category")

    
    if authors_query:
        posts = posts.filter(author__in=authors_query)
    if categories_query:
        posts = posts.filter(categories__in=categories_query).distinct() # if we are filtering with 2 filters it will return 2 item whe it has both the filter, So inorder to prevent that we use distinct()

    paginator_instance = pagination(request, posts, 9)

    context = {
        'title': "Home Page",
        'page_id': 'home',
        'paginator_instance': paginator_instance,
        'categories': categories,
        'authors': authors,
    }
    return render(request, 'web/index.html', context)


def post_page(request, id):
    context = {
        'title': "Post Page",
        'page_id': 'single-page-home',
        'post': get_object_or_404(Post.objects.filter(id=id)),
    }
    return render(request, 'web/post.html' , context)