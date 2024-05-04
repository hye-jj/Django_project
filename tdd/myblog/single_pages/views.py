from django.shortcuts import render

# Create your views here.

def about_me(request):
    return render(
        request,
        template_name="single_pages/about_me.html",
    )

def landing(request):
    return render(
        request,
        template_name="single_pages/landing.html",
    )