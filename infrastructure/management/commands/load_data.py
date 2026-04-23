from django.core.management.base import BaseCommand
from infrastructure.data.initial_data import load_initial_data


class Command(BaseCommand):
    help = 'Carga datos iniciales de Star Wars'

    def handle(self, *args, **kwargs):
        load_initial_data()
        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))