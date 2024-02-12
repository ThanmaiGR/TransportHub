from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.


def home(request):
    return render(request=request,
                  template_name='core/home.html',
                  context={})


def main(request):
    return render(request=request,
                  template_name='core/main.html',
                  context={})
