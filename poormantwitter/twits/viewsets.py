from rest_framework import viewsets

from .models import Tweets
from .serializer import TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer