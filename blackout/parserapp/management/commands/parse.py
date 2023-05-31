from django.core.management.base import BaseCommand
from ...services.parser import start_browser, get_page, scrap_data


class Command(BaseCommand):
    help = "Saves all collected data in JSON to DB"

    def handle(self, *args, **options):
        driver = start_browser()
        page = get_page(driver)
        counts = scrap_data(page)
        print(f"Parsed {counts} JSON rows")
