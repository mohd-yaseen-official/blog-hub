import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from posts.models import Post


def allow_self(function):
    def wrapper(request, *args, **kwargs):
        id = kwargs["pk"]
        if not Post.objects.filter(id=id, author__user=request.user).exists():
            
            if request.headers.get("x-requested-with") == "XMLHttpsRequest":
                
                response_data = {
                    "message": "You are not authorized to edit this post",
                    "title": "Unauthorized",
                    "status": "error",
                    "stable": "yes",
                    "redirect": "not",
                    "redirect_url": "",
                }

                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                return HttpResponseRedirect(reverse("web:index"))
            
        return function(request, *args, **kwargs)
    
    return wrapper