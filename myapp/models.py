from django.db import models
from django.forms import DateTimeField as FormDateTimeField
from jsonschema import ValidationError

class CustomDateTimeFormField(FormDateTimeField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('input_formats', [
            '%B, %d %Y %H:%M:%S',        # For the format like "July, 03 2016 06:00:25"
            '%Y-%m-%d %H:%M:%S.%f%z',    # With microseconds and timezone
            '%Y-%m-%d %H:%M:%S%z',        # With seconds and timezone
            '%Y-%m-%d %H:%M%z',           # Without seconds, with timezone
            '%Y-%m-%d %H:%M:%S.%f',       # With microseconds, without timezone
            '%Y-%m-%d %H:%M:%S',          # With seconds, without timezone
            '%Y-%m-%d %H:%M',             # Without seconds and timezone
        ])
        super().__init__(*args, **kwargs)

# class CustomDateTimeField(models.DateTimeField):
#     def formfield(self, **kwargs):
#         defaults = {'form_class': CustomDateTimeFormField}
#         defaults.update(kwargs)
#         return super().formfield(**defaults)

def validate_optional_integer(value):
    value = value.strip()  # Remove leading and trailing spaces
    if value == '':
        return None  # Return None for empty string
    try:
        return int(value)  # Try converting to integer
    except ValueError:
        raise ValidationError('Invalid integer value')

from django.db import models
from datetime import datetime

class CustomDateTimeField(models.DateTimeField):
    def to_python(self, value):
        if isinstance(value, datetime):
            return value
        try:
            return datetime.strptime(value, '%B, %d %Y %H:%M:%S')
        except (ValueError, TypeError):
            return value

class Insight(models.Model):
    end_year = models.CharField(max_length=100, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=255)
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100, blank=True)
    impact = models.CharField(max_length=100, blank=True)
    added = CustomDateTimeField()  # Using CustomDateTimeField for added
    published = CustomDateTimeField()
    country = models.CharField(max_length=100)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.added}"

    class Meta:
        verbose_name_plural = 'Insights'
