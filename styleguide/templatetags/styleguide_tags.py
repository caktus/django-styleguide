from textwrap import dedent, indent

from django import template
from django.template.base import Context
from django.template import defaultfilters

from styleguide import utils


register = template.Library()


@register.tag(name="example")
def do_example(parser, token):
    # Copy the parser, because we need to consume the tokens from it *twice*
    # once for a verbatim copy and once for a renderable copy
    parser_copy = template.base.Parser(
        list(parser.tokens),
        {},
        {},
        list(parser.command_stack),
    )
    parser_copy.tags = dict(parser.tags)
    parser_copy.filters = dict(parser.filters)

    tag_name, *args = token.split_contents()
    args = list(args)
    kwargs = {}

    # Parse the verbatim copy
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endexample':
            break
        if token.token_type == template.base.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.base.TOKEN_BLOCK:
            text.append('{%')
        elif token.token_type == template.base.TOKEN_COMMENT:
            text.append('{# ')
        text.append(token.contents)
        if token.token_type == template.base.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.base.TOKEN_BLOCK:
            text.append('%}')
        elif token.token_type == template.base.TOKEN_COMMENT:
            text.append(' #}')
    # return ExampleNode(nodelist.render(Context({})), (), {}, nodelist)
    text = dedent(''.join(text))

    # Reset to the original parser which hasn't been consumed from yet
    parser = parser_copy

    # # Consume from this parser to create the example node we can render
    # tag_name, *args = token.split_contents()
    # args = list(args)
    # kwargs = {}

    # Parse arguments used in the tag...
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
    return ExampleNode(text, args, kwargs, nodelist)

class ExampleNode(template.Node):
    def __init__(self, raw_code, args, kwargs, nodelist):
        self.args = args
        self.kwargs = kwargs
        self.nodelist = nodelist
        self.raw_code = raw_code
        super(ExampleNode, self).__init__()

    def render(self, context):
        return self.do_render(context, *self.args, **self.kwargs)

    def do_render(self, context, header="", lang='html', status=None, wide=False):
        output = []

        code = self.nodelist.render(context)
        code = dedent(code).strip()

        sections = utils.get_example_sections(self.raw_code)
        rendered_sections = utils.get_example_sections(code)

        if 'HTML' in sections:
            html = sections['HTML']
        elif 'TEMPLATE' in rendered_sections:
            sections['HTML'] = rendered_sections['TEMPLATE']
            html = sections['HTML']
        elif len(sections) == 0:
            html = code
            sections['HTML'] = self.raw_code
        else:
            raise ValueError("{% example %} must have exactly 1 or an HTML entry.")

        docs = sections.get('DOCS', None)

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

        if docs:
            output.append('<div class=styleguide-docs>')
            output.append(docs)
            output.append('</div>')

        output.append('<div class=styleguide-code>')

        output.append('<pre>')
        parts = sorted(sections.items(), key=lambda t:-1 if t[0]=='TEMPLATE' else 0)
        # assert 0, parts
        for lang, body in parts:
            if lang != "DOCS":
                output.append('<h4>%s</h4>' % lang)
                output.append('<code class=%s>' % lang)
                output.append(defaultfilters.force_escape(body))
                output.append('</code>')
        output.append('</pre>')

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
    for slug, sub_slugs in utils.get_styleguide_templates().items():
        name = defaultfilters.title(slug.replace('-', ' '))
        templates.append((name, slug, sub_slugs))

    return templates

@register.assignment_tag
def open_menu(path, slug, sub_slugs=None):
    path_list = list(filter(None, path.split('/')))
    if path.count('/') != 1:
        if sub_slugs:
            if len(path_list) >= 2:
                return path_list[-2] == slug and path_list[-1] in sub_slugs
            else:
                return path_list[-1] == slug
        else:
            return False

@register.filter
def make_space(str):
    return str.replace('_', ' ')
