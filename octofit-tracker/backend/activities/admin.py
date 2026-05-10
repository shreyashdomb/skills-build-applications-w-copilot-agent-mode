from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'performed_at', 'duration_minutes', 'distance_km', 'calories_burned')
    list_filter = ('activity_type', 'performed_at')
    search_fields = ('user__username', 'notes')
