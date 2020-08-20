from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from restapp.serializers import UserSerializer, RegisterUserSerializer


class UserAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'

    @action(methods=['post'],
            detail=False,
            permission_classes=[AllowAny, ],
            url_path='register',
            url_name='register',
            serializer_class=RegisterUserSerializer
            )
    def register(self, request):
        data = request.data
        print(f"data: {data}")
        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(validated_data=serializer.validated_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

