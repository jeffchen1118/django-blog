from django.shortcuts import render
# from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the most recent information on the website author 
    and allows user collaboration requests.
    Display an individual :model:`about.About`.
    **Context**
    ``about``
        An instance of :model:`about.About`.      
    ``collaborate_form``
        An instance of :model:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Collaborate form request received, I endeavour to respond within 2 working days.'
            )   
            
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )