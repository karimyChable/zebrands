def get_user_ip(request):
    """
    This function is used to get the IP of the user who makes the request

    :param: request
    :return: ip_user
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip_user = x_forwarded_for.split(",")[0]
    else:
        ip_user = request.META.get("REMOTE_ADDR")
    return ip_user
