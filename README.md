# FaceRecognitionAPI Introduction

This face detection and recognition API is built based on Google TensoFlow. Use this API to recognise people's faces, detect their gender, age and sentiments.

It is higly inspired by [FaceNet](https://github.com/davidsandberg/facenet).

![image](https://raw.githubusercontent.com/martinambition/FaceRecognitionAPI/master/screenshot.png)

# Installation
***[Note] It is currently available for Windows OS only.***

### Prerequisite
You have installed the followings on your computer:

  * Python 3.5+
  * Anaconda 
  
### Procedures
1. Import file enviorment.yml to create a new environment. 
   Please note it may take more than 10 minutes to download packages.
2. Download the face recognization models from [here](https://drive.google.com/open?id=1NRhwIGPhyhR9uqQb8EmZigEwOoirTO_8), and extract to "face_process\models"
2. Run the real time camera detection by execute the followings:
> python main.py

# Available APIs
The FaceRecognitionAPI provides following APIs to you:

* Face detection initiation

```python
## Init face API
from face_process.face_api import FaceAPI
face_api = FaceAPI()
```

* Capture and track faces

```python
## Face traction
face_api.track_faces(rec_img)
```

* Detect and match an existing face

```python
## Detect face id
face_api.detect_face_id_embeding(rec_img)
```

* Detect age, gender and sentiment

```python
## Detect age, gender and emotion
face_api.detect_age(rec_face_images)
face_api.detect_gender(rec_face_images)
face_api.detect_emotion(rec_face_images)
```

* Detect a new face and register

```python
## Register new face
face_api.register_new_face(embeding)
```


# License
FaceRecognitionAPI is released under the terms of the MIT license. For more information, see LICENSE or visit https://opensource.org/licenses/MIT.
