from django import template
from django.db.models import *

from news.models import Category, News

register = template.Library() 


# @register.simple_tag(name='get_list_categories')
# def get_categories():
#     return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cat=Sum('news__is_published')).filter(cat__gt=0)
    for item in categories:
        item.cat = int(item.cat)

    return { 
        'categories': categories,
    }