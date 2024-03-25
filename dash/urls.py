from django.urls import path
from . import views
# import views

urlpatterns = [
    # path('', views.dash, name="dash"),
    path('chart_view', views.chart_view, name="chart_view"),
    path('index', views.index, name="index"),
    path('data', views.data, name="data"),
    path('', views.index, name="index"),
]