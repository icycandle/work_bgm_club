from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from musiclink.models import MusicLink, MusicRating
from musiclink.permissions import IsOwnerOrReadOnly


class MusicLinkSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    sum_value = serializers.IntegerField(read_only=True)

    class Meta:
        model = MusicLink
        # fields = '__all__'
        exclude = ('user',)
        read_only_fields = (
            'sum_value',
            'username',
        )

class MusicLinkViewSet(viewsets.ModelViewSet):
    queryset = MusicLink.objects.all()
    serializer_class = MusicLinkSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def get_queryset(self):
        return MusicLink.objects.annotate(
            sum_value=Sum('music_rating__value')
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MusicRatingSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='user.username')
    # music_link = serializers.ReadOnlyField(source='musiclink.url')

    class Meta:
        model = MusicRating
        # fields = '__all__'
        exclude = ('user', 'create_at')

class MusicRatingViewSet(viewsets.ModelViewSet):
    queryset = MusicRating.objects.all()
    serializer_class = MusicRatingSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
