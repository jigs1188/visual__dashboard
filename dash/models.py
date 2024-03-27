# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.timezone import now
# from datetime import datetime

# # Create your models here.
# class Data(models.Model):
#     data = models.JSONField()
#     owner = models.ForeignKey('auth.User', related_name='data', on_delete=models.CASCADE)
#     date=models.DateField(default=now)

#     def __str__(self):
#         return self.data
    
# class Meta:
#     ordering = ['-date']

# class Insight(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     added = models.DateTimeField(default=now)
#     owner = models.ForeignKey('auth.User', related_name='insights', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    
# class Meta:
#     ordering = ['-added']
    
# class Chart(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     added = models.DateTimeField(default=now)
#     owner = models.ForeignKey('auth.User', related_name='charts', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class Meta:
#     ordering = ['-added']


