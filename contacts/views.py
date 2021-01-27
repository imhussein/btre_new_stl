from django.shortcuts import render, redirect
from django.contrib import messages
from contacts.models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST.get("realtor_id")
        listing = request.POST.get("listing")
        print(listing, "SOOOOOOOOOOOOOOOOOOOO")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        user_id = request.POST.get("user_id")

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        messages.success(request=request, message="Submitted")
        return redirect("/listings/" + listing_id)
