import cv2
import uuid
thumb_folder = './pics/'
def save_thumb(image):
    guid = str(uuid.uuid1())
    filename = guid + '.jpg'
    cv2.imwrite(thumb_folder+filename,image)
    return guid
