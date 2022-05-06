from blog.models import PostTag, Tag
from django import template

register = template.Library()


@register.inclusion_tag("block_tags.html")
def get_tags():
    return {"tags_list": Tag.objects.all()}
