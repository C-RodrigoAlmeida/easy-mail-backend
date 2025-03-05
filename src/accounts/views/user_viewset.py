from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from src.core.permissions import IsNotAuthenticated
from src.accounts.serializers import UserMutationSerializer
from src.accounts.models import CustomUser


@extend_schema(tags=['Account'])
class UserViewSet(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    viewsets.GenericViewSet
):
    serializer_class = UserMutationSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsNotAuthenticated()]
        
        return [permission() for permission in self.permission_classes]

    def get_object(self) -> CustomUser:
        """Returns the currently authenticated user instead of looking up by ID."""
        return self.request.user
    
    def create(self, request, *args, **kwargs) -> Response:
        """Overrides create to prevent multiple users from being created per session."""
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs) -> Response:
        """Updates the authenticated user's data."""
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs) -> Response:
        """Deletes the authenticated user's account."""
        user = self.get_object()
        user.delete()
        return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
