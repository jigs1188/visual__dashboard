from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("area", views.area, name="area"),
    path('datatable', views.datatable, name="datatable"),
    path('', views.base, name="base"),
    path('upload', views.upload, name="upload"),
    path('top', views.top, name="top"),
    path('insert_data_from_json', views.insert_data_from_json, name="insert_data_from_json"),
]



