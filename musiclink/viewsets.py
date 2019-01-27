from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from musiclink.models import MusicLink


class MusicLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicLink
        fields = '__all__'
        # exclude = ('users',)

class MusicLinkViewSet(viewsets.ModelViewSet):
    queryset = MusicLink.objects.all()
    serializer_class = MusicLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
