from django.shortcuts import render
from .models import Post

def post_list(request):
    """게시판 리스트를 정의해준다."""
    context = {'python_word': 'Python'}

    return render(request, 'post_service/post_list.html', context)
