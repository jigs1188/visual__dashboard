# myapp/management/commands/import_data.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from myapp.models import Insight

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the Insight model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='/home/jigs/Downloads/modified_file.csv')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert date strings to datetime objects
                added_date = datetime.strptime(row['added'], '%B, %d %Y %H:%M:%S')
                published_date = datetime.strptime(row['published'], '%B, %d %Y %H:%M:%S')

                # Create an instance of the Insight model
                insight = Insight(
                    end_year=row['end_year'],
                    intensity=row['intensity'],
                    sector=row['sector'],
                    topic=row['topic'],
                    insight=row['insight'],
                    url=row['url'],
                    region=row['region'],
                    start_year=row['start_year'],
                    impact=row['impact'],
                    added=added_date,
                    published=published_date,
                    country=row['country'],
                    relevance=row['relevance'],
                    pestle=row['pestle'],
                    source=row['source'],
                    title=row['title'],
                    likelihood=row['likelihood']
                )
                insight.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
