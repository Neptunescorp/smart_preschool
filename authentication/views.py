from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:

            login(request, user)

            if user.is_superuser:
                return redirect("/")

            if hasattr(user, "parent_profile"):
                return redirect("/parents/")

            return redirect("/")

        return render(
            request,
            "authentication/login.html",
            {
                "error": "Invalid username or password."
            },
        )

    return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")