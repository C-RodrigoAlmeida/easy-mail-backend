from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema

from src.accounts.models import CustomUser
from src.core.permissions import IsNotAuthenticated
from src.accounts.serializers import UserMutationSerializer

@extend_schema(tags=['Account'])
class UserViewSet(
    mixins.RetrieveModelMixin,
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

    def retrieve(self, request) -> Response:
        """Responds with currently authenticated user's info"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request) -> Response:
        """Creates user with hashed password"""
        password = request.data.pop('password', None)
        user = CustomUser(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email']
        )
        if password:
            user.set_password(password)
        user.save()

        return Response({'message': 'User created sucessfuly'}, status=status.HTTP_200_OK)

    def update(self, instance, validated_data) -> Response:
        """Updates the authenticated user's data"""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        instance.save()
        
        return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs) -> Response:
        """Deletes the authenticated user's account."""
        user = self.get_object()
        user.delete()
        return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT) 
   