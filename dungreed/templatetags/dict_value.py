from django import template

register = template.Library()


@register.filter
def dvu(value,arg):
    return value[arg]