from rest_framework import status
from rest_framework import permissions
from rest_framework import request as rest_request
from rest_framework import response as rest_response
from rest_framework.views import APIView

from users import serializers, models


class UserCreateApiView(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def post(self, request: rest_request.Request) -> rest_response.Response:
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        models.User.objects.create(**serializer.data)

        return rest_response.Response(status=status.HTTP_201_CREATED)
