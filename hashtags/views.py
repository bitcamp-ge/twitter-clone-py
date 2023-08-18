from rest_framework import viewsets
from .models import Hashtag
from .serializers import HashtagSerializer


class HashtagView(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    