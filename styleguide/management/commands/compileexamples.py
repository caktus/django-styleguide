from __future__ import print_function, unicode_literals

import os
import re
import hashlib

import django.template
from django.template.backends.django import DjangoTemplates
from django.core.management.base import BaseCommand

# Regex matching all JSX blocks in a template
R_EXAMPLE = re.compile(r'\{% *example.*%\}(.*?)\{% *endexample *%\}', re.DOTALL)
R_SECTION = re.compile(r'<!-- Stylus -->(.*?)<!--', re.DOTALL)


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '-o'
            '--output',
            action='store',
            dest='output',
        )

    def handle(self, *args, **kwargs):
        output = None
        if kwargs['output']:
            output = open(kwargs['output'], 'w')

        compile_templates(list_template_files(), output)

        if output is not None:
            output.close()


def list_template_files():
    """
    Return list of template files everywhere Django looks for them.
    """
    engines = django.template.engines

    template_dirs = []
    # 'engines' is not a dictionary, it just behaves like one in some ways
    for engine_name in engines:
        engine = engines[engine_name]
        if isinstance(engine, DjangoTemplates):
            # We only handle Django templates
            template_dirs.extend(engine.template_dirs)

    template_list = []
    for each in template_dirs:
        for dir, dirnames, filenames in os.walk(each):
            for filename in filenames:
                template_list.append(os.path.join(dir, filename))
    return template_list


def compile_templates(template_list, output=None):
    """

    """

    for template in template_list:
        first = True
        try:
            content = open(template).read()
        except IOError:
            pass
        else:
            blocks = re.findall(R_EXAMPLE, content)
            for block in blocks:
                if first:
                    # Add comment indicating the template that these blocks came from.
                    # Can help with debugging.
                    first = False
                    # print('/* %s */' % template, file=output)
                hash = hashlib.sha1(block.encode('utf-8')).hexdigest()

                if "<!-- HTML -->" in block:
                    block = re.findall(R_SECTION, block)
                    block = block[0].strip()
                    print(block, file=output)
