from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница проекта Yatube'
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title' : title,
        'text': text
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = 'Лев Толстой – зеркало русской революции.'
    subtext = 'Группа тайных поклонников графа'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = f'Записи сообщества {str(group)}'
    context = {
        'group': group,
        'posts': posts,
        'text': text,
        'title': title,
        'subtext': subtext
    }
    return render(request, template, context)
