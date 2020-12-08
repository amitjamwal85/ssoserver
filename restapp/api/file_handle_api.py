from django.contrib.auth.models import User
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from restapp.models.file_handle import Photo, Blogs


class FileListSerializer(serializers.Serializer):

    class Meta:
        model = Photo
        fields = '__all__'


class BlogsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images', read_only=True)
    title = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)

    class Meta:
        model = Blogs
        fields = ['id', 'title', 'desc', 'images']

    @staticmethod
    def get_images(obj):
        photos = Photo.objects.filter(blogs=obj)
        images = list()
        for photo in photos:
            images.append(photo.image.url)
        return images

    def create(self, validated_data):
        return Blogs.objects.create(**validated_data)


class FileHandleAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = BlogsSerializer
    # parser_classes = (FormParser, MultiPartParser)
    # queryset = Blogs.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            blog = serializer.save()
            for file_item in request.FILES.getlist('images'):
                c = Photo(blogs=blog, image=file_item)
                c.save()
            return Response(
                data=self.serializer_class(blog).data,
                status=status.HTTP_201_CREATED)

    def get(self, request):
        blogs = Blogs.objects.all()
        serializer = self.serializer_class(blogs, many=True)
        return Response({"blogs": serializer.data})


