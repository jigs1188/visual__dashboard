# from django.shortcuts import render
# import json

# def chart_view(request):
#     with open('/home/jigs/Documents/dashboard/myproject/jsondata.json') as f:
#         data = json.load(f)
#     return render(request, 'chart/chart_template.html', {'data': data})


# views.py
# import csv
# from django.shortcuts import render

# def chart_view(request):
#     data = []
#     entities = ['Intensity', 'Likelihood', 'Relevance',  'Topics', 'Region','Year', 'Country', 'City']  # Define your list of entities
#     # chart_types = {
#     #     'Intensity': 'bar',
#     #     'Likelihood': 'line',
#     #     'Relevance': 'pie',
#     #     # Add more mappings for other entities as needed
#     # }

#     with open('/home/jigs/Documents/dashboard/myproject/modified_files.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             data.append(row)

#     return render(request, 'chart/chart_template.html', {'data': data, 'entities': entities})

import csv
from django.shortcuts import render

def chart_view(request):
    data = []
    with open('/home/jigs/Documents/dashboard/myproject/modified_files.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    context = {
        'data': data,
    }
    return render(request, 'chart/data.html', context)
