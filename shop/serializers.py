from rest_framework import serializers
from .models import Shop, Picture, Category, Discount, Review


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('image','id')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'name', 'amount', 'discount_type', 'created_at', 'start_at', 'active')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'text', 'rating', 'created_at')


class ShopSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    discounts = DiscountSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'owner', 'pictures', 'phone_number', 'location', 'open_time', 'close_time', 'description',
                  'categories', 'social_media_link', 'payment_method', 'availability', 'discounts', 'availability_days',
                  'rate', 'reviews',)
