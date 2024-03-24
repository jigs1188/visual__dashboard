from django.urls import path
from . import views
# import views

urlpatterns = [
    # path('', views.dash, name="dash"),
    path('chart_view', views.chart_view, name="chart_view"),
]