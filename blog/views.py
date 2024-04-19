from django.shortcuts import render
from .models import Author,Post
from .serializers import authorSerializer,postSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .tasks import status_blog

status_blog()

class postView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=postSerializer

class postView_pk(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=postSerializer
    lookup_field='pk'

