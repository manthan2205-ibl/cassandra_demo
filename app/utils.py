from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import status, exceptions
from . models import *


def Authenticate(self, request):
    auth = get_authorization_header(request).split()
    if not auth or auth[0].lower() != b'token':
        return None

    if len(auth) == 1:
        msg = 'Invalid token header. No credentials provided.'
        raise exceptions.AuthenticationFailed(msg)
    elif len(auth) > 2:
        msg = 'Invalid token header'
        raise exceptions.AuthenticationFailed(msg)

    try:
        token = auth[1]
        if token == "null":
            msg = 'Null token not allowed'
            raise exceptions.AuthenticationFailed(msg)
    except UnicodeError:
        msg = 'Invalid token header. Token string should not contain invalid characters.'
        raise exceptions.AuthenticationFailed(msg)

    return token


from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status'] = response.status_code
        if response.data.get('detail'):
            response.data['message'] = response.data['detail'] 
            response.data.pop("detail")
        response.data['results'] = []
        
        print(response.data)

    return response