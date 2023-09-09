from rest_framework.serializers import ModelSerializer
from .models import Service, Tag, ServiceReview


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class ServiceReviewSerializer(ModelSerializer):
    class Meta:
        model = ServiceReview
        fields = '__all__'