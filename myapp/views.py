from django.shortcuts import render, redirect
from .models import Registration

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender= request.POST.get("gender")
        message = request.POST.get("message")
        country=request.POST.get("country")

        # Save to database
        Registration.objects.create(
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            message=message,
            country=country
        )

        # Redirect to success page
        return redirect('register_success')

    return render(request, "base.html")


def success(request):
    return render(request, "success.html")
