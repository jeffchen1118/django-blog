from django.shortcuts import render
# from django.views import generic
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Display an individual :model:`about.About`.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about_detail.html`
    """

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    return render(
        request,
        "about/about_me.html",
        {"about": about},
        {"collaborate_form": collaborate_form},
        )