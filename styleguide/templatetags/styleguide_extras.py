from django import template

from styleguide import utils


register = template.Library()


@register.assignment_tag
def get_styleguide_templates():
    return utils.get_styleguide_templates()
