from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by(
        "-list_date").filter(is_published=True)[:4]
    context = {
        "title": "Homepage",
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "price_choices": price_choices,
    }
    return render(request, "pages/index.html", context)


def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    seller = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "title": "About",
        "realtors": realtors,
        "seller": seller
    }
    return render(request, "about/about.html", context)
