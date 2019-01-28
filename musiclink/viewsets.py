from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from musiclink.models import MusicLink
from musiclink.permissions import IsOwnerOrReadOnly


class MusicLinkSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MusicLink
        # fields = '__all__'
        exclude = ('user',)

class MusicLinkViewSet(viewsets.ModelViewSet):
    queryset = MusicLink.objects.all()
    serializer_class = MusicLinkSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
