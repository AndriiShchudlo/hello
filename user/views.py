# Create your views here.
import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import BaseUser


@api_view(['POST'])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not password or not username:
        return Response(status=400, data={"msg": "Bad request"})
    user = BaseUser.objects.get(username=username, password=password)
    if not user:
        return Response(status=400, data={"msg": "Bad request"})
    token =  f"FS{uuid.uuid4().hex}"
    user.mobile_token = token
    user.save()
    return Response(status=200, data={"token": token})


