from django import template

register = template.Library()



@register.filter
def tildemin(value):
    if "~" in value:
        return value.split()[0] 
    else:
        return value

@register.filter
def tildemax(value):
    if "~" in value:
        return value.split()[2] 
    else:
        return value

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

@register.filter
def rd(value):
    if '*2*' in value:
        return [1,2]
    elif '*3*' in value:
        return [1,2,3]
    elif '*4*' in value:
        return [1,2,3,4]
    elif '*5*' in value:
        return [1,2,3,4,5]
    else:
        return [1]

@register.filter
def cf(value):
    if '초록' in value:
        return '초록'
    elif '빨강' in value:
        return '빨강'
    elif '주황' in value:
        return '주황'
    elif '보라' in value:
        return '보라'
    elif '파랑' in value:
        return '파랑'
    elif '노랑' in value:
        return '노랑'
    else:
        return ''