from django.shortcuts import get_object_or_404, render
from django import forms


class ExampleForm(forms.Form):
    text = forms.CharField()
    disabled_text = forms.CharField(disabled=True)
    checkbox1 = forms.BooleanField()
    checkbox2 = forms.BooleanField()
    select = forms.ChoiceField(choices=[('',  "Select an Option"), (1, 'one'), (2, 'two'), (3, 'three')])
    radio = forms.ChoiceField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], widget=forms.RadioSelect())

form_initial = {
    "disabled_text": "This field can't be changed",
}


def styleguide(request):
    return render(request, "styleguide/styleguide.html", {

    })

def styleguide_page(request, name):
    return render(request, "styleguide/styleguide-%s.html" % name, {
        "example_form": ExampleForm(initial=form_initial),
    })
def styleguide_sub_page(request, name, sub_page):
    return render(request, "styleguide/styleguide-%s-%s.html" % (name, sub_page), {
        "example_form": ExampleForm(initial=form_initial),
    })
