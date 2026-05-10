from django.conf import settings
from django.db import models


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('run', 'Running'),
        ('walk', 'Walking'),
        ('strength', 'Strength Training'),
        ('cycle', 'Cycling'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities',
    )
    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_TYPE_CHOICES,
        default='other',
    )
    performed_at = models.DateTimeField(auto_now_add=True)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-performed_at', '-created_at']

    def __str__(self):
        return f"{self.user} - {self.get_activity_type_display()} on {self.performed_at.date()}"
