from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm

class HomeNews(ListView):
    model = News
    # template_name = 'news/home_news_list.html'
    # context_object_name = 'news'
    # extra_context = {'title': "Главная"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    # template_name = 'news/home_news_list.html'
    # context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)   


class ViewNews(DetailView):
    model = News
    template_name = 'news/news_detail.html' 
    # context_object_name = 'news_item' 


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'




# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#          }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id = category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     context = {
#         'news':news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context) 


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item':news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form':form})