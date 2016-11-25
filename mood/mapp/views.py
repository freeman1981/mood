from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.contrib.auth.models import User

from .models import Mood
from .serializers import MoodSerializer, UserSerializer


class MoodViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
