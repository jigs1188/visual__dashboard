# views.py
import json
from django.utils import timezone  # Import timezone module
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Insight
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "index.html")

def area(request):
    return render(request, "area.html")
def datatable(request):
    return render(request, "datatable.html")

def upload(request):
    return render(request, "upload.html")


def base(request):
    return render(request, "base.html")

# def insights(request):
#     return render(request, "insights.html")

def insert_data_from_json(request):
    if request.method == 'POST':
        json_file = request.FILES.get('json_file')
        if json_file:
            data = json.loads(json_file.read().decode('utf-8'))

            for record in data:
                try:
                    # Convert 'added' field to datetime object
                    added_date = datetime.strptime(record["added"], '%B, %d %Y %H:%M:%S')
                    published_date = datetime.strptime(record["published"], '%B, %d %Y %H:%M:%S')
                except ValueError:
                    return JsonResponse({'error': 'Invalid datetime format'}, status=400)

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
                    added=added_date,
                    # published=record["published"],
                    published=published_date,
                    country=record["country"],
                    relevance=record["relevance"],
                    pestle=record["pestle"],
                    source=record["source"],
                    title=record["title"],
                    likelihood=record["likelihood"]
                )

            return JsonResponse({'message': 'Data inserted successfully'})
        else:
            return JsonResponse({'error': 'No JSON file uploaded'}, status=400)
    else:
        return render(request, 'upload_form.html')

# views.py
    
def top(request):
    top_entries = Insight.objects.all()[:5]
    return render(request, 'top.html', {'top_entries': top_entries})
