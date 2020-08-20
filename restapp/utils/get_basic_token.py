from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField( required=True )


class GetBasicTokenView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        print("data:", data)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

            user_data = User.objects.get(username=user)
            resp_data = dict()
            resp_data['email'] = user_data.email
            resp_data['username'] = user_data.username
            token, _ = Token.objects.get_or_create(user=user)
            resp_data['token'] = token.key
            return Response(resp_data, status=HTTP_200_OK)
