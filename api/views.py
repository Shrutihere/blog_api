from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from .models import Blog
from .serializer import UserSerializer, BlogSerializer, RegisterSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     user = self.request.user
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

