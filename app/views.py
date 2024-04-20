from django.shortcuts import render
from .models import Post

# 1. Циклом измените все заголовки моделей на тот же заголовок, но + id.
# Пример: «заголовок (id)».
# 2. Удалите записи, которые имеют нечётную цифру в заголовке.


def index(request):
    posts = Post.objects.all()
    newpost = []
    for post in posts:
        if post.id % 2 != 0:
            newpost.append(post)
    return render(request, "index.html", {"posts": posts, "newpost": newpost})
