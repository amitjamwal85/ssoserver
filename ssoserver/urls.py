from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework import routers
from simple_sso.sso_server.server import Server

from restapp.utils.get_basic_token import GetBasicTokenView
from restapp.views import UserAPIView
from rest_framework_simplejwt import views as jwt_views

test_server = Server()

urlpatterns = [
    path('admin/', admin.site.urls),

    # SSO URLS
    url(r'^server/', include(test_server.get_urls())),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Basic Token
    path('user/login/', GetBasicTokenView.as_view(), name="user-login"),

    # JWT Token
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

router = routers.SimpleRouter()
router.register(r'users', UserAPIView)
urlpatterns += router.urls
