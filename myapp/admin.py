from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Insight

class InsightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Insight._meta.fields]  # Display all fields

admin.site.register(Insight, InsightAdmin)
