"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    http post http://127.0.0.1:8000/api/token/ username=multivendor password=multiadmin

    http http://127.0.0.1:8000/api/vendors "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MTU5NTE2LCJpYXQiOjE2NjcxNTkyMTYsImp0aSI6IjNhNzBiYzJlODdmMjQ2YzZiNjQ1YTBiZjA3YWRjMDVmIiwidXNlcl9pZCI6MX0.uJBcX8kcXie7GNM7MF2jAP2riyWFBhHpi-mCfswH1H0"

    http http://127.0.0.1:8000/api/token/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzI0NTYxNiwiaWF0IjoxNjY3MTU5MjE2LCJqdGkiOiIyMmI2ZGY3Y2E5ZWM0OTFjOGE1OGE2N2JhNmIyOThjZSIsInVzZXJfaWQiOjF9.WNr1OcdS_B64C2JtkWjOiamE69i3e0FeZO7AZ_m2BBI"


    """
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]
