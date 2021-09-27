import os
import shutil
import datetime

from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from mainApp.api.serializer import RegisterSerializer
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from mainApp.models import Device
from mainApp.models import Face
from mainApp.models import KnownFace
from web.pusher import push_notification

import base64

from django.core.files.base import ContentFile


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


class GetFaces(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        try:
            faces = Face.objects.filter(user=user)
        except:
            faces = None
        outputs = []
        for face in faces:
            output = {
                'link': face.pic_link,
                'date': str(face.datetime).split(' ')[0],
                'time': (str(face.datetime).split(' ')[1]).split('.')[0]
            }
            outputs.append(output)
        return Response(outputs)


class GetKnownFaces(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        try:
            faces = KnownFace.objects.filter(user=user)
        except:
            faces = None
        outputs = []
        for face in faces:
            output = {
                'link': face.pic_link,
                'name': face.first_name + ' ' + face.last_name,
            }
            outputs.append(output)
        return Response(outputs)


class AddFace(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        img = request.data.get('img')
        name = request.data.get('name')
        family = request.data.get('family')
        format, imgstr = img.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        my_dir = 'pics/' + user.username + '/'
        if not os.path.isdir(my_dir):
            os.makedirs(my_dir)
        img_loc = my_dir + name + '_' + family + '.png'
        img_link = 'http://127.0.0.1:8000/media/' + img_loc
        with open(img_loc, 'wb') as f:
            shutil.copyfileobj(data.file, f, length=131072)
        known_face = KnownFace(first_name=name, last_name=family, user=user, pic_address=img_loc, pic_link=img_link)
        known_face.save()
        return Response('عملیات با موفقیت انجام شد.')


class Test(APIView):
    def get(self, request):
        return Response(push_notification.send_notification('hello'))


class Ring(APIView):

    def post(self, request):
        img = request.data.get('img')
        device_id = request.data.get('device_id')
        device = Device.objects.get(serial=device_id)
        user = device.user
        print(img)
        imgstr = img
        data = ContentFile(base64.b64decode(imgstr), name='temp.png')
        my_dir = 'rings/' + user.username + '/'
        if not os.path.isdir(my_dir):
            os.makedirs(my_dir)
        img_loc = my_dir + str(datetime.datetime.now().date()) + str(datetime.datetime.now().time()) + '.png'
        img_link = 'http://127.0.0.1:8000/media/' + img_loc
        with open(img_loc, 'wb') as f:
            shutil.copyfileobj(data.file, f, length=131072)
        face = Face( user=user, pic_address=img_loc, pic_link=img_link)
        face.save()
        return Response('عملیات با موفقیت انجام شد.')
