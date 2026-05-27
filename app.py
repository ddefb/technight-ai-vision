from flask import Flask, render_template, Response

from keras.models import load_model
from keras.preprocessing.image import img_to_array

import cv2
import numpy as np

app = Flask(__name__)

# =========================================================
# LOAD MODELS
# =========================================================

face_classifier = cv2.CascadeClassifier(
    'haarcascades/haarcascade_frontalface_default.xml'
)

classifier = load_model(
    'models/model.h5'
)

emotion_labels = [
    'Angry',
    'Disgust',
    'Fear',
    'Happy',
    'Neutral',
    'Sad',
    'Surprise'
]

# =========================================================
# VIDEO STREAM
# =========================================================

def generate_frames():

    cap = cv2.VideoCapture(0)

    # Better resolution for TV
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:

        success, frame = cap.read()

        if not success:
            break

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_classifier.detectMultiScale(
            gray,
            1.3,
            5
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 255, 255),
                2
            )

            roi_gray = gray[y:y+h, x:x+w]

            roi_gray = cv2.resize(
                roi_gray,
                (48, 48),
                interpolation=cv2.INTER_AREA
            )

            if np.sum([roi_gray]) != 0:

                roi = roi_gray.astype('float') / 255.0

                roi = img_to_array(roi)

                roi = np.expand_dims(
                    roi,
                    axis=0
                )

                prediction = classifier.predict(
                    roi,
                    verbose=0
                )[0]

                label = emotion_labels[
                    prediction.argmax()
                ]

                label_position = (x, y - 10)

                cv2.putText(
                    frame,
                    label,
                    label_position,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    'No Face Found',
                    (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

        ret, buffer = cv2.imencode(
            '.jpg',
            frame
        )

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()

# =========================================================
# ROUTES
# =========================================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )