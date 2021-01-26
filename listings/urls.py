from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("search", views.search, name="search")
]
