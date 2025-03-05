from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from src.accounts.serializers import AuthSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request) -> Response:
        serializer = AuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        
        user = authenticate(username=email, password=password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
