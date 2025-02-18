from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)   
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = [
        "new_building",
        "town",
        "rooms_number",
        "has_balcony",
        "active",
        "floor",
    ]
    raw_id_fields = ["likes"]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]
    list_display = ["user", "flat"]
    search_fields = ["user__username", "flat__address", "message"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("name", "phonenumber", "normalized_number")
    raw_id_fields = ["flats"]