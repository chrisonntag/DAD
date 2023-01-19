from rest_framework import serializers
from .models import Exhibition, Item, MediaType, Favorite, Like, Comment
from users.serializers import UserSerializer


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ('id', 'start_date', 'end_date', 'name', 'description')

class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        fields = ('id', 'description', 'media_type_name')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'related_to', 'part_of', 'type_of', 'name', 'description', 'digital_copy')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'item', 'date')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'item', 'date')

class FullCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'item', 'title', 'content', 'date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'item', 'title', 'content', 'date')



