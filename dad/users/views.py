from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, DADTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UsersAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        # Return REST Response
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


class DADTokenObtainPairView(TokenObtainPairView):
    serializer_class = DADTokenObtainPairSerializer

