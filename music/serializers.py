from rest_framework import serializers
from .models import Music


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ("name", "artists")
