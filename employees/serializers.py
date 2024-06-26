from rest_framework.serializers import ModelSerializer

from .models import Employee, Idea

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "fullname", "dep", "birthdate", "salary", "created_at"]

class IdeaSerializer(ModelSerializer):
    class Meta:
        model = Idea
        fields = ["id", "userName", "thumbsUppCount", "thumbsDownCount", "idea", "created_at"]
