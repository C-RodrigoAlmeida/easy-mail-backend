from rest_framework import routers

from src.contacts.views import RecipientViewSet, RecipientGroupViewSet


router = routers.SimpleRouter()

router.register('recipient', RecipientViewSet)
router.register('group', RecipientGroupViewSet)

urlpatterns = router.urls