from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee, Idea
from .serializers import EmployeeSerializer, IdeaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class IdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    @action(detail=True, methods=['patch'])
    def update_thumbs_count(self, request, pk=None):
        print('update_thumbs_count')
        idea = self.get_object()
        print('idea', idea)
        # Assuming your request has thumbsUppCount and thumbsDownCount in the data
        thumbs_up_count = request.data.get('thumbsUppCount')
        thumbs_down_count = request.data.get('thumbsDownCount')

        print('thumbs_up_count', thumbs_up_count)
        print('thumbs_down_count', thumbs_down_count)

        # Perform the update
        idea.thumbsUppCount = thumbs_up_count
        idea.thumbsDownCount = thumbs_down_count
        idea.save()

        serializer = self.get_serializer(idea)
        return Response(serializer.data, status=status.HTTP_200_OK)