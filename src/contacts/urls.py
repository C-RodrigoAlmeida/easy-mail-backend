from rest_framework import routers

from src.contacts.views import RecipientViewSet


router = routers.SimpleRouter()

router.register('recipient', RecipientViewSet)

urlpatterns = router.urls