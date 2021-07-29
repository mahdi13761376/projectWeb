from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from mainApp.api.views import RegisterView
from mainApp.views import HelloView
from django.contrib import admin

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='auth_register'),

]
