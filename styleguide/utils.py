import os
import re
from django import template


def get_styleguide_templates(styleguide_dirs=None):
    """Walk selected directories and pull out valid filenames"""
    if not styleguide_dirs:
        styleguide_dirs = get_styleguide_dirs()
    template_paths = {}
    sub_template_paths = []
    for template_dir in styleguide_dirs:
        for (dirpath, dirnames, filenames) in os.walk(template_dir):
            for filename in filenames:
                match = re.search(r'^styleguide-([\w-]+)\.html$', filename)
                if match:
                    if '-' not in match.group(1):
                        template_paths[match.group(1)] = []
                    else:
                        sub_menu_item = match.group(1).split('-')
                        sub_template_paths.append(sub_menu_item)

    for sub in sub_template_paths:
        if sub[0] in template_paths:
            template_paths[sub[0]].append(sub[1])

    return template_paths


def get_styleguide_dirs():
    """Find all styleguide/ dirs within all Django template dirs"""
    template_dirs = []
    engines = template.engines.all()
    for engine in engines:
        for loader in engine.engine.template_loaders:
            for template_dir in loader.get_template_sources('styleguide'):
                if os.path.isdir(str(template_dir)):
                    template_dirs.append(str(template_dir))
    return template_dirs

def get_example_sections(example):
    """Parses a multipart example and returns them in a dictionary by type.

    Types will be by language to highlight, except the special "__doc__"
    section. The default section is "html".
    """

    parts = re.split(r'<!-- (.*) -->', example)
    del parts[0]
    i = iter(parts)

    sections = {}
    for lang, code in zip(i, i):
        sections[lang] = code.strip()
    return sections
