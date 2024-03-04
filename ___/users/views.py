from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("core:home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == 'password2':
                        messages.error(request, f"Confirm Password: {error}")
                    else:
                        messages.error(request, f"{field}: {error}")
            return render(request=request,
                          template_name="users/register.html",
                          context={"form": form})
    form = NewUserForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
    )


def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged out successfully!")
    return redirect("core:home")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('core:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
    )


def account(request):
    if request.method == "POST":
        return redirect("users:edit")

    if request.user.is_authenticated:
        return render(
            request=request,
            template_name="users/account.html",
            context={}
        )
    else:
        messages.error(request, 'Please login to view account details')
        return redirect("users:login")


def edit(request):
    if request.method == "POST":
        email = request.POST.get('aemail')
        fname = request.POST.get('afirst')
        lname = request.POST.get('alast')
        if (fname == '') and (lname != ''):
            messages.error(request, "First name cannot be blank with Last Name")
            return render(
                request=request,
                template_name="users/edit.html",
                context={}
            )
        user = None
        try:
            user = get_object_or_404(User, email=email)
            if user is not None:
                if user == request.user:
                    request.user.email = email
                    request.user.first_name = fname
                    request.user.last_name = lname
                    request.user.save()
                    messages.success(request, "Profile updated")
                    return redirect("core:home")
                else:
                    messages.error(request, "Email Already Exists")
        except Exception:
            request.user.email = email
            request.user.first_name = fname
            request.user.last_name = lname
            request.user.save()
            messages.success(request, "Email Successfully Changed")
            return redirect("core:home")
    if request.user.is_authenticated:
        return render(
            request=request,
            template_name="users/edit.html",
            context={}
        )
    else:
        messages.error(request, 'Please login to view account details')
        return redirect("users:login")
