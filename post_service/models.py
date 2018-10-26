from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    게시물 model을 정의해준다.
    """
    # 게시물의 제목, 1024자로 제한
    title = models.CharField(max_length=1024)
    # 게시물의 내용, 자유롭게 글을 쓸수있게 한다.
    content = models.TextField()
    # 게시물의 작성자는 Django의 기본 User를 이용
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # 게시물의 작성 시간, 자동으로 게시물이 등록되는 시간이 설정 되도록 하자.
    date_added = models.DateTimeField(auto_created=True, auto_now_add=True)
