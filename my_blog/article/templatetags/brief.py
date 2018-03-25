import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

# 自定义file时必须加上
register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def brief(value):
    value = value[:50]
    result = mark_safe(
        markdown.markdown(
            value,
            extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
            safe_mode=True,
            enable_attributes=False
            )
        )
    
    return result