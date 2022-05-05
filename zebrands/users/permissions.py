from rest_framework import permissions
from rest_framework import exceptions
from django.contrib.auth.models import Group

from django.db import connection
import logging


class PermissionRequired(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            raise_exception = True

            app_label = view.model._meta.app_label
            model_name = view.model._meta.model_name
            method = request.method.lower()
            available_methods = ['get']  # Only get methods are availables for anonymous users
            available_tables = ['product']
            # If the request method is a get, all users can see the information
            if method in available_methods and model_name in available_tables:
                return True
            # Here we're going to validate the method requested via API
            else:
                user = request.user
                if user.is_staff:
                    return True
                else:
                    raise Exception("No tienes permiso para realizar esta accion")
                    return False
        except Exception as error:
            return False
