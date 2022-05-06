import time

from zebrands.logs.models import Log
from zebrands.utils.ip_users import get_user_ip


class LogMiddleware:
    """
    This middleware Intercept the request and save it only is a product request
     on table Log
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        execution_time = time.time()
        response = self.get_response(request)  # Get response from view function.
        execution_time = int((time.time() - execution_time)*1000)

        # Returns only the response if not from products
        prefixs = [
            '/api/v1/products'
        ]
        methods_to_store = ['GET']
        method_requested = request.method
        if not list(filter(request.get_full_path().startswith, prefixs)) or method_requested not in methods_to_store:
            return response

        # Save on Log Table
        request_log = Log(
            endpoint=request.get_full_path(),
            status_code=response.status_code,
            method=request.method,
            ip=get_user_ip(request),
            exec_time=execution_time,
            body_response=str(response.content),
            body_request=str(request.body)
        )

        # Save user if admin
        if not request.user.is_anonymous:
            request_log.user = request.user

        # Save log in db
        request_log.save()
        return response
