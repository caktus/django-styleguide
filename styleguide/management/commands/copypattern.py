import os
import shutil

from django.apps import apps
from django.core.management.base import LabelCommand, CommandError
from django import template
from styleguide.utils import get_styleguide_templates


class Command(LabelCommand):
    help = 'Copy built-in pattern from the styleguide to project templates'

    def handle_label(self, label, **options):
        source_name, source_path = self.get_template_path(label)
        try:
            project_templates = template.engines.templates['django']['DIRS'][0]
        except (KeyError, IndexError):
            raise CommandError("Project template DIRS not found")
        dest_dir = os.path.join(project_templates, "styleguide")
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
        dest_path = os.path.join(dest_dir, source_name)
        if os.path.isfile(dest_path):
            raise CommandError("{} already exists".format(dest_path))
        shutil.copy(source_path, dest_path)

    def get_template_path(self, slug):
        app_config = apps.get_app_config('styleguide')
        template_name = "styleguide-{}.html".format(slug)
        template_path = os.path.join(app_config.path, "templates/styleguide",
                                     template_name)
        if not os.path.isfile(template_path):
            raise CommandError("Pattern '{}' not found".format(slug))
        return template_name, template_path
