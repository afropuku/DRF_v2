from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewset, PostViewSet


router = SimpleRouter()
router.register('users', UserViewset)
router.register('', PostViewSet)

urlpatterns = router.urls
