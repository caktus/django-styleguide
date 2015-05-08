from textwrap import dedent

from django import template
from django.template import defaultfilters

from styleguide import utils


register = template.Library()


@register.tag(name="example")
def do_example(parser, token):
    tag_name, lang = token.contents.split(None, 1)
    nodelist = parser.parse(('endexample',))
    parser.delete_first_token()
    return ExampleNode(lang, nodelist)

class ExampleNode(template.Node):
    def __init__(self, lang, nodelist):
        self.lang = lang
        self.nodelist = nodelist
        super(ExampleNode, self).__init__()

    def render(self, context):
        output = []

        code = self.nodelist.render({})
        code = dedent(code).strip()

        output.append("<div class=styleguide-example>")
        output.append("<div class=styleguide-code>")

        output.append("<pre><code class=%s>" % self.lang)
        output.append(defaultfilters.force_escape(code))
        output.append("</code></pre>")

        output.append("</div>")
        output.append("<div class=styleguide-demo>")

        output.append(code)

        output.append("</div></div>")

        return ''.join(output)


@register.assignment_tag
def get_styleguide_templates():
    """Return tuples of (display name, slug) for found styleguide templates"""
    templates = []
    for slug in utils.get_styleguide_templates():
        name = defaultfilters.title(slug.replace('-', ' '))
        templates.append((name, slug))
    return templates
