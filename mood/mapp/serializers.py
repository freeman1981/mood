from django.contrib.auth.models import User
from .models import Mood
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'mood_value', 'datetime', 'owner')
        read_only_fields = ('owner',)
