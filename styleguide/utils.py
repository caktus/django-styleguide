import os
from django import template


def get_styleguide_templates():
    """Walk selected directories and pull out filenames"""
    template_paths = []
    for template_dir in get_styleguide_dirs():
        for (dirpath, dirnames, filenames) in os.walk(template_dir):
            template_paths.extend(filenames)
    return template_paths


def get_styleguide_dirs():
    """Find all styleguide/ dirs within all Django template dirs"""
    template_dirs = []
    engines = template.engines.all()
    for engine in engines:
        # Reverse template_loaders to search apps first, followed by project
        # templates, so the built-in styleguide templates are list first.
        for loader in reversed(engine.engine.template_loaders):
            for template_dir in loader.get_template_sources('styleguide'):
                if os.path.isdir(template_dir):
                    template_dirs.append(template_dir)
    return template_dirs
