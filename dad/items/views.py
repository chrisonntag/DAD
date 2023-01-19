from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Exhibition, MediaType, Item, Favorite, Like, Comment
from django.contrib.auth.models import User
from .serializers import ExhibitionSerializer, MediaTypeSerializer, ItemSerializer, FavoriteSerializer, LikeSerializer, CommentSerializer, FullCommentSerializer
from users.serializers import UserSerializer
from model_bakery import baker
from model_bakery.random_gen import gen_email, gen_text, gen_image_field
from datetime import datetime
from django.db.models import Count
from rest_framework_simplejwt import authentication


class ItemListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Item.objects.all()

        # Shows top N items of a specific exhibition sorted by the number of comments per item, compare M1.
        famous = self.request.query_params.get('famous')
        exhibition_name = self.request.query_params.get('exhibition')

        if famous is not None:
            try:
                famous = int(famous)
            except ValueError:
                return Response({'error': 'GET parameter famous must be a number'}, status=status.HTTP_400_BAD_REQUEST)
            
            famous_comments_queryset = Comment.objects.values('item').annotate(comments_count=Count('item')).order_by('-comments_count').values('item')

            if exhibition_name is not None:
                queryset = queryset.filter(pk__in=famous_comments_queryset, part_of__name=exhibition_name)[:famous]
            else:
                queryset = queryset.filter(pk__in=famous_comments_queryset)[:famous]

        serializer = ItemSerializer(queryset, many=True)

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
        serializer = FullCommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        username = authentication.JWTAuthentication().authenticate(request)[0]
        user = User.objects.filter(username=username).first()
        item = Item.objects.filter(pk=pk).first()

        print(user)

        if item is None:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'user': user.id,
            'item': item.id,
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'date': datetime.now()
        }

        serializer = CommentSerializer(data=data)

        print(serializer.initial_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        username = authentication.JWTAuthentication().authenticate(request)[0]
        user = User.objects.filter(username=username).first()

        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        favorites = Favorite.objects.filter(user=user).values_list('item')
        items = Item.objects.filter(pk__in=favorites)
        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        username = authentication.JWTAuthentication().authenticate(request)[0]
        user = User.objects.filter(username=username).first()
        item = Item.objects.filter(pk=pk).first()

        if item is None:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'user': user.id,
            'item': item.id,
            'date': datetime.now()
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
        exhibition_recipe = baker.make_recipe('items.exhibition_artscape', _quantity=1)
        media_recipe = baker.make_recipe('items.media_img')
        item_fourtytwo_recipe = baker.make_recipe('items.item_fourtytwo', _create_files=True, digital_copy=gen_image_field, _quantity=6)
        item_echoes_recipe = baker.make_recipe('items.item_echoes', _create_files=True, digital_copy=gen_image_field, _quantity=9)
        fav_recipe = baker.make_recipe('items.fav')
        comment_recipe = baker.make_recipe('items.comment_el', _quantity=12)
        comment_ad_recipe = baker.make_recipe('items.comment_ad', _quantity=3)

        return Response({'SUCCESS'}, status=status.HTTP_200_OK)


