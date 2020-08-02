from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # view to return token to user when they log-in.

from core.views import TestView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name = 'obtain-token'),
    path('rest-auth/', include('rest_auth.urls'))
]
