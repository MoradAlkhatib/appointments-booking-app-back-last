from rest_framework import generics, response
from .models import Shop
from .serializers import ShopSerializer, PictureSerializer
from rest_framework.decorators import api_view

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


@api_view(['POST'])
def UploadImageView(request):
    serializer = PictureSerializer(data=request.data)
    try :
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        
    except Exception as e:
        return response.Response(str(e))
    

    
