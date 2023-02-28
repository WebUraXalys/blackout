from django.core.management.base import BaseCommand
from ...services.parser import start_browser, get_page


class Command(BaseCommand):
    help = "Saves all collected data in JSON to DB"

    def handle(self, *args, **options):
        driver = start_browser()
        counts = get_page(driver)
        print(f"Parsed {counts} JSON rows")
