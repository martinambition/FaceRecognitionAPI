# FaceRecognitionAPI

This is a tensoflow based face recognization which enable to detect gender, age and emotion.
It is higly inspired by [FaceNet](https://github.com/davidsandberg/facenet).

![image](https://raw.githubusercontent.com/martinambition/FaceRecognitionAPI/master/screenshot.png)

## Installation

### Requirements

  * Python 3.5+
  * Anaconda

### Installation on Windows:
1. Install [Anaconda](https://www.anaconda.com/download/).
2. Create a new enviorment by importing enviorment.yml.(It may 10+ minutes to download packages)



## Instructions
### Run real time detection for camera:
> python main.py

## API
The FaceRecognitionAPI provides several apis to track face and detect features.

```python
## Init face API
from face_process.face_api import FaceAPI
face_api = FaceAPI()
```


```python
## Face traction
face_api.track_faces(rec_img)
```


```python
## Detect face id
face_api.detect_face_id_embeding(rec_img)
```

```python
## Detect age, gender and emotion
face_api.detect_age(rec_face_images)
face_api.detect_gender(rec_face_images)
face_api.detect_emotion(rec_face_images)
```

```python
## Register new face
face_api.register_new_face(embeding)
```


## License
FaceRecognitionAPI is released under the terms of the MIT license. See LICENSE for more information or see https://opensource.org/licenses/MIT.