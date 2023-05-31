from django.contrib import admin
from admin_extra_buttons.api import ExtraButtonsMixin, button
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer

from .models import Streets, Buildings, Interruptions
from .services.parser import start_browser, get_page, save_data, scrap_data
from .services.generators import generate_streets, generate_emergency_interruption, generate_plan_interruption, generate_planned_interrupted_buildings


@admin.register(Streets)
class StreetsAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ["pk", "Name", "City", "OTG", "Region"]
    ordering = ["Name"]

    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def parse(self, request):
        driver = start_browser()
        page = get_page(driver)
        counts = scrap_data(page)

        self.message_user(request, f"Parser finished. Saved in JSON {counts} rows")

        return HttpResponseRedirectToReferrer(request)

    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def save(self, request):
        save_data()

        self.message_user(request, "Saved all jsons")

        return HttpResponseRedirectToReferrer(request)
    
    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def generate_streets(self, request):
        generate_streets()

        self.message_user(request, "Streets generated")

        return HttpResponseRedirectToReferrer(request)
    

@admin.register(Buildings)
class BuildingsAdmin(ExtraButtonsMixin, admin.ModelAdmin):
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

    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def generate_planned_interrupted_buildings(self, request):
        if Streets.objects.exists() and Interruptions.objects.filter(Type="Plan").exists():
            generate_planned_interrupted_buildings()
            self.message_user(request, "Buildings and interruption generated")
        else:
            self.message_user(request, "Firstly create Streets and Interruptions!!!")
        
        return HttpResponseRedirectToReferrer(request)

    def get_type_interruption(self, obj):
        if obj.Interruption:
            return obj.Interruption.Type
        return None

    get_type_interruption.short_description = "Type Interruption"


@admin.register(Interruptions)
class InterruptionAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ["pk", "Start", "End", "Type"]
    ordering = ["pk"]

    @button(html_attrs={'style': 'background-color:#FFA500;color:black'})
    def generate_emergency_interruption(self, request):
        generate_emergency_interruption()

        self.message_user(request, "Interruptions generated")

        return HttpResponseRedirectToReferrer(request)
    
    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def generate_plan_interruption(self, request):
        generate_plan_interruption()

        self.message_user(request, "Interruptions generated")

        return HttpResponseRedirectToReferrer(request)
