from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet,TodoStatusViewSet

router = DefaultRouter()
router.register(r"todo", TodoViewSet)
router.register(r"todostatus", TodoStatusViewSet)

urlpatterns = [
        path("", include(router.urls)),
]
# urlpatterns += router.urls