from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from mainApp.api.views import RegisterView, AddFace, Ring, Open
from mainApp.api.views import Initialize
from mainApp.api.views import AddDevice
from mainApp.api.views import ChangePassword
from mainApp.api.views import ChangeDevice
from mainApp.api.views import GetFaces
from mainApp.api.views import GetKnownFaces
from mainApp.api.views import Test
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('ini/', Initialize.as_view(), name='hello'),
    path('add_device/', AddDevice.as_view(), name='hello'),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_pass/', ChangePassword.as_view(), name='change_pass'),
    path('change_device/', ChangeDevice.as_view(), name='change_device'),
    path('get_faces/', GetFaces.as_view(), name='get_faces'),
    path('get_known_faces/', GetKnownFaces.as_view(), name='get_known_faces'),
    path('add_face/', AddFace.as_view(), name='add_face'),
    path('open/', Open.as_view(), name='open'),
    path('ring/', Ring.as_view(), name='ring'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
