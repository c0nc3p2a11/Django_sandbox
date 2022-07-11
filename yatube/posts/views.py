from django.shortcuts import render, get_object_or_404
from .models import Post, Group


TEN_CONST = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('author').all()[:TEN_CONST]
    title = 'Это главная страница проекта Yatube'
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
        'text': text
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = 'Лев Толстой – зеркало русской революции.'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:TEN_CONST]
    title = f'Записи сообщества {str(group)}'
    context = {
        'group': group,
        'posts': posts,
        'text': text,
        'title': title
    }
    return render(request, template, context)
