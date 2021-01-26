from django.db.models import query
from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.


def listings(request):
    listings = Listing.objects.order_by("list_date").filter(is_published=True)
    per_page = 3
    paginator = Paginator(listings, per_page)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)
    context = {
        "title": "Listings",
        "listings": paged_listings
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing,
        "title": f"Listing {listing_id}",
    }
    return render(request, "listings/listing.html", context=context)


def search(request):
    query_list = Listing.objects.order_by("-list_date")
    if 'keywords' in request.GET:
        keywords = request.GET.get("keywords")
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET.get("city")
        if city:
            query_list = query_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET.get("state")
        if state:
            query_list = query_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET.get("price")
        if price:
            query_list = query_list.filter(price__lte=price)

    context = {
        "title": "Search Page",
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "price_choices": price_choices,
        "query_list": query_list,
        "values": request.GET
    }
    return render(request, "listings/search.html", context)

# Fix Login Page - Add New Style
# Overview And View More Less Size And Center
# Revenu Remove The Broder Left
# Overview Popup Increase Padding
# Table Header Remove Propties And Stella Tower In all 4 tabs
# Widgets Size
# View Btn Change Style
# Change Font style For DropDown
# Empty Popup For View In Reports Page
