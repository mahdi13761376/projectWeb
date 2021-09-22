import glob

import face_recognition
import numpy as np

from mainApp.models import Device, KnownFace


def my_face_recognition(user, img):
    user_directory = 'pics/' + user.username
    user_device = Device(user=user)
    faces = []
    names = []
    for x in glob.glob(user_directory):
        face = face_recognition.load_image_file(user_directory + x)
        face_encoding = face_recognition.face_encodings(face)[0]
        faces.append(face_encoding)
        names.append(x.split('.')[0])

    in_img = face_recognition.load_image_file(img)
    in_img_enc = face_recognition.face_encodings(in_img)[0]
    face_distances = face_recognition.face_distance(faces, in_img_enc)
    best_match_index = np.argmin(face_distances)
    if 100 - face_distances[best_match_index] > user_device.accuracy:
        return KnownFace(user=user, first_name=names[best_match_index].split('_')[0],
                         last_name=names[best_match_index].split('_')[1] )
    return None
