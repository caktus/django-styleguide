import os

from django.shortcuts import get_object_or_404, render
from django.conf import settings

import markdown

from .forms import EverythingBagelForm, everything_bagel_form_initial, CreateUserForm, create_user_form_initial

def styleguide(request):
    path = os.path.join(settings.BASE_DIR, 'README.md')
    if os.path.exists(path):
        contents = open(path).read()
    else:
        contents = ""
    return render(request, "styleguide/styleguide.html", {
        "contents": markdown.markdown(contents),
    })

def styleguide_page(request, name):
    return render(request, "styleguide/styleguide-%s.html" % name, {
        "everything_bagel_form": EverythingBagelForm(initial=everything_bagel_form_initial),
        "create_user_form": CreateUserForm(initial=create_user_form_initial),
    })
def styleguide_sub_page(request, name, sub_page):
    return render(request, "styleguide/styleguide-%s-%s.html" % (name, sub_page), {
        "everything_bagel_form": EverythingBagelForm(initial=everything_bagel_form_initial),
        "create_user_form": CreateUserForm(initial=create_user_form_initial),
    })
