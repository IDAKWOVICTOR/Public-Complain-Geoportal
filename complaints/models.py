from django.contrib.gis.db import models

class Complaint(models.Model):
    COMPLAINT_TYPES = [
        ('Accident', 'Accident'),
        ('Water Leakage', 'Water Leakage'),
        ('Pothole', 'Pothole'),
        ('Borehole', 'Borehole'),
        ('Broken Facility', 'Broken Facility'),
    ]

    complaint_type = models.CharField(max_length=50, choices=COMPLAINT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', null=True, blank=True)
    location = models.PointField(srid=4326)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complaint_type} at {self.location}"
