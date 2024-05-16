from rest_framework import serializers
from .models import video_model
class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model=video_model
        fields="__all__"