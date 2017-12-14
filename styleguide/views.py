from django.shortcuts import get_object_or_404, render
from .forms import EverythingBagelForm, everything_bagel_form_initial, CreateUserForm, create_user_form_initial

def styleguide(request):
    return render(request, "styleguide/styleguide.html", {

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
