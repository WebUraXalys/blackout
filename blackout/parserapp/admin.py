from django.contrib import admin
from admin_extra_buttons.api import ExtraButtonsMixin, button
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer

from .models import Streets, Buildings, Interruptions
from .services.parser import start_browser, get_page, save_data


@admin.register(Streets)
class StreetsAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ["pk", "Name", "City", "OTG", "Region"]
    ordering = ["Name"]

    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def run_script(self, request):
        driver = start_browser()
        counts = get_page(driver)

        self.message_user(request, f"Parser finished. Saved in JSON {counts} rows")

        return HttpResponseRedirectToReferrer(request)


@admin.register(Buildings)
class BuildingsAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "Address",
        "Street",
        "Group",
        "Interruption",
        "get_type_interruption",
        "Longitude",
        "Latitude",
    ]
    ordering = ["pk"]

    def get_type_interruption(self, obj):
        if obj.Interruption:
            return obj.Interruption.Type
        return None

    get_type_interruption.short_description = "Type Interruption"


@admin.register(Interruptions)
class InterruptionAdmin(admin.ModelAdmin):
    list_display = ["pk", "Start", "End", "Type"]
    ordering = ["pk"]
