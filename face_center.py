import numpy as np
from face_process.face_api import FaceAPI
from thumb.thumb_center import *


def detect_camera(cameraid,callback,show_screen = True):
    face_api = FaceAPI()
    camera = cv2.VideoCapture(cameraid)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
    while True:
        ret, frame = camera.read()
        rec_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_h, img_w, _ = np.shape(rec_img)
        bounding_boxes = face_api.track_faces(rec_img)
        faces_count = len(bounding_boxes)
        rec_face_images =[]
        for index in range(faces_count):
            face_position = bounding_boxes[index][1]
            left, top, right, bottom = face_position[0], face_position[1], face_position[2], face_position[3]
            if left < 0 or top < 0 or right > img_w or bottom > img_h:
                continue
            rec_face_images.append(rec_img[top:bottom + 1, left:right + 1, :])

        if len(rec_face_images)>0:
            age_result = face_api.detect_age(rec_face_images)
            gender_result = face_api.detect_gender(rec_face_images)
            emotion_result = face_api.detect_emotion(rec_face_images)

            for index,(trackid, box) in enumerate(bounding_boxes):
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                label = "{},{},{}".format(age_result[index],gender_result[index], emotion_result[index])#age_result[index][1]
                cv2.putText(frame, label, (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0),
                        thickness=2, lineType=2)
            if callback:
                callback(age_result, gender_result, emotion_result)
        if show_screen:
            cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('r'):
            break