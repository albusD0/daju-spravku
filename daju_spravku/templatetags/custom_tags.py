from django import template
from daju_spravku.models import Category, Tag

register = template.Library()


@register.inclusion_tag('daju_spravku/list_categories.html')
def show_categories(active_category=0):
    return {'topics': Category.objects.all(), 'active_category': active_category}

@register.inclusion_tag('daju_spravku/list_tags.html')
def show_all_tags():
    return {"tags": Tag.objects.all()}