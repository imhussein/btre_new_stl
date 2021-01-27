from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request=request, user=user)
            messages.success(request=request, message="Logged in successfully")
            return redirect("dashboard")
        else:
            messages.error(request=request, message="Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html", context={
            "title": "Login"
        })


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        user_name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            if User.objects.filter(username=user_name).exists():
                messages.error(request=request, message="Username is taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request=request, message="Email is taken")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request=request, message="Successfully Registered")
                    return redirect("login")
        else:
            messages.error(request, "Password don't match")
            return redirect("register")
    else:
        return render(request, "accounts/register.html", context={
            "title": "Register"
        })


def logout(request):
    if request.method == 'POST':
        auth.logout(request=request)
        messages.success(request=request, message="Logged out")
        return redirect("index")


def dashboard(request):
    return render(request, "accounts/dashboard.html", context={
        "title": "Dashboard"
    })
