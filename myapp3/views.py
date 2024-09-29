from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Author, Post


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ...
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')


def post_detail(self, request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Some title",
        "content": "Some content"
    }

    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': 'John'}
    return render(request, 'myapp3/my_template.html', context)


class TempleIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Привет, мир'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        '1': 'один',
        '2': 'два',
        '3': 'три',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)


def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_post.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
