from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Plant
from .serializers import PlantSerializer

class PlantListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        plants = Plant.objects.filter(owner=request.user)
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Set the owner automatically
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlantDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk, owner=request.user)
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk, owner=request.user)
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlantSerializer(plant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk, owner=request.user)
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
