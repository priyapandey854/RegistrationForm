from django.shortcuts import render, redirect
from .models import Registration

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Save to database
        Registration.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Redirect to success page
        return redirect('register_success')

    return render(request, "base.html")


def success(request):
    return render(request, "success.html")
