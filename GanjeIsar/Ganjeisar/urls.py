
from django.contrib import admin
from django.urls import path ,include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

urlpatterns = [
    path('Gi/admin/', admin.site.urls),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('Gi/users/' , include('users.urls')),

    path('Gi/posts/',include('posts.urls')),


    path('Gi/martyr/',include('martyrs.urls')) ,
]
