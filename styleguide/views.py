from django.shortcuts import get_object_or_404, render


def styleguide(request):
    return render(request, "styleguide/styleguide.html", {

    })

def styleguide_page(request, name):
    return render(request, "styleguide/styleguide-%s.html" % name, {

    })
def styleguide_sub_page(request, name, sub_page):
    return render(request, "styleguide/styleguide-%s-%s.html" % (name, sub_page), {

    })
