import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Log(models.Model):
    """
    Stores the list of endpoint called in the system
     :model:`auth.User` - Save user if user is not anonymous
     Other attributes for this model are:
     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    endpoint = Url from endpoint
    status_code = The status code for the response
    method = Method requested
    ip = User IP who call the endpoint
    exec_time = Execution time
    body_response = Body of the response
    body_request = Body of the request
    created_at = Date of creation log
    updated_at = Date from log update
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    endpoint = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status_code = models.PositiveSmallIntegerField()
    method = models.CharField(max_length=10, null=True)
    ip = models.CharField(max_length=20, null=True)
    exec_time = models.IntegerField(null=True)
    body_response = models.TextField()
    body_request = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
