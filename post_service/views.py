from django.shortcuts import render, redirect
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login

def post_list(request):
    """게시판 리스트를 정의해준다."""
    page_data = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')

    if page is None:
        page = 1
    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = {'post_list': posts, 'current_page': page,
        'totla_page':range(1, page_data.num_pages + 1)}

    return render(request, 'post_service/post_list.html', context)
