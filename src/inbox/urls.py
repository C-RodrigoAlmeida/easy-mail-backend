from rest_framework import routers

from src.inbox.views import TemplateViewSet

router = routers.SimpleRouter()

router.register('template', TemplateViewSet)

urlpatterns = router.urls