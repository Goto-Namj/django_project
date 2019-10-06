from django import template

register = template.Library()


@register.filter
def dvu(value,arg):
    return value[arg]

@register.filter
def aom(value):
    if '+' in value:
        return '+'
    elif '-' in value:
        return '-'
    else:
        return 0
