from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from zebrands.users.permissions import PermissionRequired
from zebrands.users.serializers import (
    GetUserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
)


class UserView(APIView):
    """
    Display methods for get, update or delete a User Item :model:`auth.User`.
    """

    model = User
    permission_classes = [PermissionRequired]

    def get(self, request, pk):
        """
        Endpoint to get a User Item :model:`auth.User`.
        """
        try:
            user = User.objects.get(pk=pk)
            user_serializer = GetUserSerializer(user)
            return Response(
                dict(success=True, data=user_serializer.data), status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                dict(success=False, error="Usuario no encontrado"),
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk):
        """
        Endpoint to get update a User Item :model:`auth.User`.
        """
        try:
            user = User.objects.get(pk=pk)
            user_serializer = UserUpdateSerializer(
                user, data=request.data, partial=True
            )
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(
                    dict(
                        success=False,
                        errors=[
                            x + "-" + y[0]
                            for x, y in zip(
                                user_serializer.errors.keys(),
                                user_serializer.errors.values(),
                            )
                        ],
                    ),
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as error:
            return Response(
                dict(success=False, errors=["Ocurrio un error al editar el usuario"]),
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        """
        Endpoint to delete a User Item :model:`auth.User`.
        """
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(
                dict(success=False, errors=["El usuario no existe"]),
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserListView(APIView):
    """
    Display methods for Save and list all Users Items. User Item :model:`auth.User`.
    """

    model = User
    permission_classes = [PermissionRequired]

    def get(self, request):
        """
        Method for get a list of all User Item. User Item :model:`auth.User`.
        """
        users = User.objects.all()
        users_serializer = GetUserSerializer(users, many=True)
        return Response(
            dict(success=True, data=users_serializer.data, status=status.HTTP_200_OK)
        )

    def post(self, request):
        """
        Method for save a User Item. User Item :model:`auth.User`.
        """
        try:
            user_serializer = UserCreateSerializer(data=request.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    dict(
                        success=False,
                        errors=[
                            x + "-" + y[0]
                            for x, y in zip(
                                user_serializer.errors.keys(),
                                user_serializer.errors.values(),
                            )
                        ],
                    ),
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as error:
            return Response(
                dict(success=False, errors=["Ocurri?? un error al guardar el usuario"]),
                status=status.HTTP_400_BAD_REQUEST,
            )
