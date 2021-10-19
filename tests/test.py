import glob
import json
import sys
import os
import face_recognition
import ast
import numpy as np


class NumpyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


# # print('salam')
# # user_directory = '/home/mahdi/Documents/karshenasi/codes/web/web/pics/' + user.username + '/'
# # user_device = Device.objects.get(user=user)
# # faces = []
# # names = []
# # for x in glob.glob(user_directory + '*'):
# #     print(x)
# #     face = face_recognition.load_image_file(x)
# #     face_encoding = face_recognition.face_encodings(face)[0]
# #     faces.append(face_encoding)
# #     names.append((x.split('/')[-1]).split('.')[0])
# import numpy as np
#
user_directory = '/home/mahdi/PycharmProjects/pythonProject2/lfw/'
data = {}
i = 0
if os.path.isfile('data.txt'):
    final_data = {}
    with open('data.txt', 'r') as f:
        data = json.loads(f.read())
        for key in data.keys():
            if key not in final_data.keys():
                final_data[key] = []
            for face in data[key]:
                final_data[key].append(np.array(face))
    correct = 0
    all = 0
    false_pos = 0
    false_neg = 0
    for key in final_data.keys():
        for face in final_data[key]:
            for key2 in final_data.keys():
                for face2 in final_data[key2]:
                    all += 1
                    check = face_recognition.compare_faces(face, [face2], 0.1)
                    if key == key2:
                        if check[0]:
                            correct += 1
                        else:
                            false_neg += 1
                    if key != key2:
                        if check[0]:
                            false_pos += 1
                        else:
                            correct += 1
    print('false pos: ' + str(false_pos / all))
    print('false neg: ' + str(false_neg / all))
    print('correct: : ' + str(correct / all))


else:
    for dir in glob.glob(user_directory + '*'):
        name = dir.split('/')[-1]
        if name not in data.keys():
            data[name] = []
        for file in glob.glob(dir + '/*'):
            face = face_recognition.load_image_file(file)
            face_encodings = face_recognition.face_encodings(face)
            if len(face_encodings):
                face_encoding = face_recognition.face_encodings(face)[0]
                data[dir.split('/')[-1]].append(face_encoding)
            else:
                print(file)
    print(data)
    original_stdout = sys.stdout
    with open('data.txt', 'w') as f:
        sys.stdout = f
        print(json.dumps(data, cls=NumpyEncoder))
        sys.stdout = original_stdout

# in_img = face_recognition.load_image_file('test/Andre_Agassi_0001.jpg')
# faces = []
# face = face_recognition.load_image_file('test/Andre_Agassi_0034.jpg')
# face_encoding = face_recognition.face_encodings(face)[0]
# faces.append(face_encoding)
# in_img_enc = face_recognition.face_encodings(in_img)[0]
# face_distances = face_recognition.compare_faces(faces, in_img_enc)
# print(face_distances)
