from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from mainApp.api.serializer import RegisterSerializer
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        output = {}
        output['name'] = user.first_name
        return Response(output)
