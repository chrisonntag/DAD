from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Exhibition, MediaType, Item, Favorite, Like, Comment
from django.contrib.auth.models import User
from .serializers import ExhibitionSerializer, MediaTypeSerializer, ItemSerializer, FavoriteSerializer, LikeSerializer, CommentSerializer
from model_bakery import baker
from model_bakery.random_gen import gen_email, gen_text, gen_image_field


class ItemListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        item = Item.objects.filter(pk=pk).first()  # Returns the object or None

        if item is None:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK) 


class CommentAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        item = Item.objects.filter(pk=pk).first()

        if item is None:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(item=item)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        item = Item.objects.filter(pk=pk).first()

        if item is None:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'user': request.user.id,
            'item': item.id,
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'date': request.data.get('date')
        }

        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.id).first()

        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        favorites = Favorite.objects.filter(user=user).values_list('item')
        items = Item.objects.filter(pk__in=favorites)
        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        item = Item.objects.filter(pk=request.data.get('pk')).first()

        if item is None:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'user': request.user.id,
            'item': item.id,
            'date': request.data.get('date')
        }

        serializer = FavoriteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FillAPIView(APIView):
    def get(self, request, *args, **kwargs):
        User.objects.all().delete()
        Exhibition.objects.all().delete()
        MediaType.objects.all().delete()
        items = Item.objects.all()
        for item in items:
            item.delete()
        Favorite.objects.all().delete()
        Comment.objects.all().delete()

        user_ad_recipe = baker.make_recipe('items.user_ad')
        user_el_recipe = baker.make_recipe('items.user_el')
        exhibition_recipe = baker.make_recipe('items.exhibition_artscape')
        media_recipe = baker.make_recipe('items.media_img')
        item_fourtytwo_recipe = baker.make_recipe('items.item_fourtytwo', _create_files=True, digital_copy=gen_image_field, _quantity=6)
        item_echoes_recipe = baker.make_recipe('items.item_echoes', _create_files=True, digital_copy=gen_image_field, _quantity=9)
        fav_recipe = baker.make_recipe('items.fav')
        comment_recipe = baker.make_recipe('items.comment_el', _quantity=12)

        return Response({'SUCCESS'}, status=status.HTTP_200_OK)

