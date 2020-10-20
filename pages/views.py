from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post

def index(request):
    posts= Post.objects.all()

    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context= {
        'posts': paged_posts,
    }

    return render(request, 'pages/index.html', context)
