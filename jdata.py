import json
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Import your Django model
from myapp.models import Insight

# Read the JSON file
json_file_path = '/home/jigs/Documents/dashboard/myproject/jsondata.json'
try:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"JSON file not found at {json_file_path}")
    exit(1)
except json.JSONDecodeError:
    print(f"Error decoding JSON file at {json_file_path}")
    exit(1)

# Insert data into the database
for record in data:
    try:
        Insight.objects.create(
            end_year=record["end_year"],
            intensity=record["intensity"],
            sector=record["sector"],
            topic=record["topic"],
            insight=record["insight"],
            url=record["url"],
            region=record["region"],
            start_year=record["start_year"],
            impact=record["impact"],
            added=record["added"],
            published=record["published"],
            country=record["country"],
            relevance=record["relevance"],
            pestle=record["pestle"],
            source=record["source"],
            title=record["title"],
            likelihood=record["likelihood"]
        )
    except Exception as e:
        print(f"Error inserting record: {e}")

print("Data inserted successfully.")
