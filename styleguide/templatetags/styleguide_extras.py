import re

from django import template
from django.template.defaultfilters import title
from styleguide import utils


register = template.Library()


@register.assignment_tag
def get_styleguide_templates():
    """Return tuples of (display name, slug) for found styleguide templates"""
    templates = []
    for template_ in utils.get_styleguide_templates():
        match = re.search(r'^styleguide-([\w-]+)\.html$', template_)
        if match:
            slug = match.group(1)
            name = title(slug.replace('-', ' '))
            templates.append((name, slug))
    return templates
