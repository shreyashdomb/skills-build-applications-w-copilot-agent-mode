from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Activity

User = get_user_model()


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'user',
            'activity_type',
            'performed_at',
            'duration_minutes',
            'distance_km',
            'calories_burned',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
