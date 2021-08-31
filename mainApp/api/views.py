from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from mainApp.api.serializer import RegisterSerializer
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from mainApp.models import Device


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class Initialize(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        try:
            device = Device.objects.get(user=user)
        except:
            device = None
        output = {}
        output['name'] = user.first_name
        output['username'] = user.username
        output['last_name'] = user.last_name
        if device is not None:
            output['device'] = device.serial
            output['device_acc'] = device.accuracy
            output['device_mode'] = device.mode
        return Response(output)


class AddDevice(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        acc = request.GET['acc']
        mode = request.GET['mode']
        id = request.GET['id']
        print(acc)
        try:
            device = Device.objects.get(serial=id)
        except:
            device = None
        if device is None:
            return Response('سریال وارد شده معتبر نیست.', 401)
        else:
            device.accuracy = acc
            device.mode = mode
            device.user = user
            device.save()
            output = {}
            output['device_acc'] = device.accuracy
            output['device_mode'] = device.mode
            return Response(output)


class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        password = request.GET['password']
        if len(password):
            user.set_password(password)
            user.save()
            return Response('رمز عبور شما تغییر کرد.')
        return Response('مشکلی پیش آمده است.')


class ChangeDevice(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        acc = request.GET.get('acc', '')
        mode = request.GET.get('mode', '')
        print(mode)
        try:
            device = Device.objects.get(user=user)
        except:
            device = None
        if device is None:
            return Response('مشکلی پیش آمده است.')
        else:
            if len(acc):
                device.accuracy = acc
            if len(mode):
                device.mode = mode

        device.save()
        return Response('اطلاعات دستگاه شما به‌روزرسانی شد.')
