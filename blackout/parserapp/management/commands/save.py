from django.core.management.base import BaseCommand
from ...services.parser import save_data


class Command(BaseCommand):
    help = "Saves all collected data in JSON to DB"

    def handle(self, *args, **options):
        save_data()
