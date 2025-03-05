from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth import login

from drf_spectacular.utils import extend_schema

from src.accounts.serializers import UserAuthSerializer

@extend_schema(tags=['Auth'])
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserAuthSerializer

    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data) 
        
        if serializer.is_valid():
            user = serializer.validated_data['user'] 
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
