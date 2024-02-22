from . import viewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'employees', viewsets.EmployeeViewSet)

urlpatterns = router.urls
