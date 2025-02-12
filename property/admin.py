from django.contrib import admin
from .models import Flat, Complaint, Owner


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


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]
    list_display = ["user", "flat"]
    search_fields = ["user__username", "flat__address", "complaint_test"]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "owners_phonenumber", "owner_pure_phone")
    raw_id_fields = ["flats"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
