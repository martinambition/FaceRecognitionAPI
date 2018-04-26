import sys
import os
from face_center import *

def handle_face_detect_result(ages, genders, emotions):
    print(ages[0], genders[0], emotions[0])
detect_camera(0, handle_face_detect_result)

