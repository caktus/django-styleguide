from textwrap import dedent

from django import template
from django.template import defaultfilters

from styleguide import utils


register = template.Library()


@register.tag(name="example")
def do_example(parser, token):
    tag_name, *args = token.split_contents()
    args = list(args)
    kwargs = {}
    def decode(value):
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
        return value
    while args and '=' in args[-1]:
        key, value = args.pop(-1).split('=', 1)
        kwargs[key] = decode(value)
    args = [decode(arg) for arg in args]
    nodelist = parser.parse(('endexample',))
    parser.delete_first_token()
    return ExampleNode(args, kwargs, nodelist)

class ExampleNode(template.Node):
    def __init__(self, args, kwargs, nodelist):
        self.args = args
        self.kwargs = kwargs
        self.nodelist = nodelist
        super(ExampleNode, self).__init__()

    def render(self, context):
        return self.do_render(*self.args, **self.kwargs)

    def do_render(self, header="", lang='html', status=None, wide=False):
        output = []

        code = self.nodelist.render(template.Context({}))
        code = dedent(code).strip()

        if '<!-- HTML -->' in code:
            html = code.split('<!-- HTML -->', 1)[1]
        else:
            html = code


        if header or status:
            output.append('<h4 class="%s">%s</h4>' % (
                (' styleguide-status-'+status if status else ''),
                header,
            ))
        classes = ['styleguide-example']
        if wide:
            classes.append('styleguide-example-wide')
        classes = ' '.join(classes)
        output.append('<div class="%s">' % classes)
        output.append('<div class=styleguide-code>')

        output.append('<pre><code class=%s>' %  lang)
        output.append(defaultfilters.force_escape(code))
        output.append('</code></pre>')

        output.append('</div>')
        output.append('<div class=styleguide-sep><span>➵</span></div>')
        output.append('<div class=styleguide-demo>')

        output.append(html)

        output.append('</div></div>')

        return ''.join(output)


@register.assignment_tag
def get_styleguide_templates():
    """Return tuples of (display name, slug) for found styleguide templates"""
    templates = []
    for slug in utils.get_styleguide_templates():
        name = defaultfilters.title(slug.replace('-', ' '))
        templates.append((name, slug))
    return templates
