from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from simple_sso.sso_server.server import Server

from restapp.api.celery_api import celery_task
from restapp.api.file_handle_api import FileHandleAPI
from restapp.api.test_inheritance_serializer import BillingTransactionListRestApi
from restapp.utils.get_basic_token import GetBasicTokenView
from restapp.utils.get_oauth2_jwt_token import SocialConvertTokenView
from restapp.api.user_api import UserAPIView
from rest_framework_simplejwt import views as jwt_views

# test_server = Server()

urlpatterns = [
    path('admin/', admin.site.urls),

    # SSO URLS
    # url(r'^server/', include(test_server.get_urls())),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Basic Token
    path('user/login/', GetBasicTokenView.as_view(), name="user-login"),

    # JWT Token
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # OAuth Social
    path('auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^custom-auth/convert-token/', SocialConvertTokenView.as_view(), name='auth_create'),

    # Celery
    path('celery_task/', celery_task),

    # Files Upload
    path('files_upload/', FileHandleAPI.as_view()),

    # Inheritance  test
    path('billing_transactions/', BillingTransactionListRestApi.as_view()),
]

router = routers.SimpleRouter()
router.register(r'users', UserAPIView)
urlpatterns += router.urls
