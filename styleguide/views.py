from django.shortcuts import get_object_or_404, render
from .forms import ExampleForm, example_form_initial, SimpleForm, simple_form_initial

def styleguide(request):
    return render(request, "styleguide/styleguide.html", {

    })

def styleguide_page(request, name):
    return render(request, "styleguide/styleguide-%s.html" % name, {
        "example_form": ExampleForm(initial=example_form_initial),
        "simple_form": SimpleForm(initial=simple_form_initial),
    })
def styleguide_sub_page(request, name, sub_page):
    return render(request, "styleguide/styleguide-%s-%s.html" % (name, sub_page), {
        "example_form": ExampleForm(initial=example_form_initial),
        "simple_form": SimpleForm(initial=simple_form_initial),
    })
