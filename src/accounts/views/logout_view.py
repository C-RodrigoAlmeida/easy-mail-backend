from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import logout

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Auth'])
class LogoutView(APIView):
    def post(self, request) -> Response:
      logout(request)
      return Response(status=status.HTTP_204_NO_CONTENT)
        