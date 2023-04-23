import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from Shopping_app.models import Volcano_data

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **options):
        try:
            with open(str(base_dir)+ '/Shopping_app/data/Volcano_data.csv', newline = '', encoding='iso-8859-1', errors='ignore') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    print(row)
                    volcano.id = row[0]
                    volcano.volcano_name = row[1]
                    volcano.volcano_image = row[2]
                    volcano.volcano_type = row[3]
                    volcano.country = row[4]
                    volcano.region = row[5]
                    volcano.subregion = row[6]
                    volcano.epoch_period = row[7]
                    volcano.summit_and_elevation = row[8]
                    volcano.latitude = row[9]
                    volcano.longitude = row[10]
                    volcano.save()

            self.stdout.write(self.style.SUCCESS('Data imported successfully.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found at {file_path}.'))

        except csv.Error as e:
            self.stdout.write(self.style.ERROR(f'Error reading CSV file: {e}'))
