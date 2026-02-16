from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    def create(self, request):
        property_id = request.data.get('property_id')
        if Favorite.objects.filter(user=request.user, property_id=property_id).exists():
            return Response({'detail': 'Already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        
        favorite = Favorite.objects.create(user=request.user, property_id=property_id)
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_201_CREATED)