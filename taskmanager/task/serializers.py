from rest_framework import serializers
from .models import Task  # Adjust this import based on your app

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Use this to include all model fields, or list specific fields
