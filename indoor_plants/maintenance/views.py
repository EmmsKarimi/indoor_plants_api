from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Maintenance
from .serializers import MaintenanceSerializer

class MaintenanceListView(APIView):
    def get(self, request):
        maintenance_tasks = Maintenance.objects.all()
        serializer = MaintenanceSerializer(maintenance_tasks, many=True)
        return Response(serializer.data)

class MaintenanceCreateView(APIView):
    def post(self, request):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceDetailView(APIView):
    def get(self, request, pk):
        try:
            maintenance_task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(maintenance_task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            maintenance_task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(maintenance_task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            maintenance_task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        maintenance_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
