from django import template
register=template.Library()
def swap(value):
    return value.swapcase()
@register.filter('sp')
def splitting(value,arg):
    return value.split(arg)
@register.filter('up')
def upper(value):
    return value.upper()
@register.filter('lw')
def lower(value):
    return value.lower()
register.filter('swapping',swap)
#register.filter('splitting',splitting)
# register.filter('uppering',upper)
#register.filter('lowring',lower)