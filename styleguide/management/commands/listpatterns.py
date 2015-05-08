import os

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from styleguide.utils import get_styleguide_templates


class Command(BaseCommand):
    help = 'List built-in patterns from the styleguide'

    def handle(self, *args, **options):
        app_config = apps.get_app_config('styleguide')
        template_dir = os.path.join(app_config.path, "templates/styleguide")
        for slug in get_styleguide_templates([template_dir]):
            print(slug)
