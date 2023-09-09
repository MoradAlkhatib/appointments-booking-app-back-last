from django.urls import path
from .views import ShopList, ShopDetail, UploadImageView

urlpatterns = [
    path('', ShopList.as_view()),
    path('<int:pk>/', ShopDetail.as_view()),
    path('image/',UploadImageView),
  
]
