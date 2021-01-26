from realtors.models import Realtor
from django.contrib import admin


class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "hire_date")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
