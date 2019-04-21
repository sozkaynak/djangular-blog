from rest_framework.routers import DefaultRouter
from .api import TopicViewSet, PostViewSet

router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
