from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema

from src.accounts.serializers import AuthSerializer
from src.core.permissions import IsNotAuthenticated

@extend_schema(tags=['Auth'])
class LoginView(APIView):
  permission_classes = [IsNotAuthenticated()]

  def post(self, request) -> Response:
    """Handles login requests"""

    serializer = AuthSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]
    
    user = authenticate(request, username=email, password=password)
    if not user:
      return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    login(request, user)
    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

@extend_schema(tags=['Auth'])
class SessionView(APIView):
  permission_classes = [AllowAny]
  
  def get(self, request) -> Response:
    """Checks session authentication"""

    return Response({"isAuthenticated": request.user.is_authenticated}, status=status.HTTP_200_OK)

@extend_schema(tags=['Auth'])
class LogoutView(APIView):
  """Handles logout requests"""

  def post(self, request) -> Response:
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
        