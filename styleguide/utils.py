import os
import re
from django import template


def get_styleguide_templates(styleguide_dirs=None):
    """Walk selected directories and pull out valid filenames"""
    if not styleguide_dirs:
        styleguide_dirs = get_styleguide_dirs()
    template_paths = set()
    for template_dir in styleguide_dirs:
        for (dirpath, dirnames, filenames) in os.walk(template_dir):
            for filename in filenames:
                match = re.search(r'^styleguide-([\w-]+)\.html$', filename)
                if match:
                    template_paths.add(match.group(1))
    return sorted(template_paths)


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
