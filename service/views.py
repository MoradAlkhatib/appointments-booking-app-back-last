from .models import *
from rest_framework import status,generics
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class serviceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = []

class serviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = []


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = []
    
class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = []
    
class ServiceReviewList(generics.ListCreateAPIView):
    queryset = ServiceReview.objects.all()
    serializer_class = ServiceReviewSerializer
    authentication_classes = []
    
class ServiceReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceReview.objects.all()
    serializer_class = ServiceReviewSerializer
    authentication_classes = []
        
