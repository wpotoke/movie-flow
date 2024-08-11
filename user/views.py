from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from user.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():

            remember_me = form.cleaned_data.get("remember_me")
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)
            if user:
                backend = (
                    user.backend
                    if hasattr(user, "backend")
                    else "django.contrib.auth.backends.ModelBackend"
                )
                auth.login(request, user, backend=backend)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 недели
                else:
                    request.session.set_expiry(
                        0
                    )  # Закрыть сессию при закрытии браузера

                return HttpResponseRedirect(reverse("index:index"))
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "user/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = (
                    user.backend
                    if hasattr(user, "backend")
                    else "django.contrib.auth.backends.ModelBackend"
                )
            auth.login(request, user, backend=backend)
            return HttpResponseRedirect(reverse("index:index"))
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "user/registration.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index:index"))


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {"form": form}
    return render(request, "user/profile.html", context)
