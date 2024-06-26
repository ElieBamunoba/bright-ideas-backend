from django.urls import path

from rest_framework import routers
from .views import EmployeeViewSet, IdeaViewSet

router = routers.DefaultRouter()

router.register('employees', EmployeeViewSet)
router.register('ideas', IdeaViewSet)

urlpatterns = router.urls