from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_social_oauth2.views import ConvertTokenView
from oauth2_provider.models import AccessToken
from rest_framework.views import APIView
import json
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from six import text_type


class SocialConvertTokenSerializer(serializers.Serializer):
    grant_type = serializers.CharField(required=True, help_text='convert_token')
    client_id = serializers.CharField(required=True)
    client_secret = serializers.CharField(required=True)
    backend = serializers.CharField(required=True)
    token = serializers.CharField(required=True)


class SocialConvertTokenView(ConvertTokenView, APIView):
    permission_classes = (AllowAny,)
    serializer_class = SocialConvertTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Use the rest framework `.data` to fake the post body of the django request.
        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value

        url, headers, body, status_code = self.create_token_response(request._request)

        if 'error' in body:
            return Response(json.loads(body), status=status.HTTP_400_BAD_REQUEST)

        try:
            oauth_token = AccessToken.objects.get(token=json.loads(body).get('access_token'))
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        print("OAuth token user : ", oauth_token.user)

        token = RefreshToken.for_user(oauth_token.user)
        data = {
            'access': text_type(token.access_token),
            'refresh': text_type(token),
        }
        return Response(data, status=status.HTTP_201_CREATED)
