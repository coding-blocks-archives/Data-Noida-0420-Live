import cv2
import numpy as np
import os

import os
from sklearn.neighbors import KNeighborsClassifier

data = np.load("faces.npy")

X, y = data[:, 1:], data[:, 0]

model = KNeighborsClassifier()
model.fit(X, y)

cap = cv2.VideoCapture(1)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)



        if len(faces) > 0:

            for face in faces:
                x, y, w, h = face

                cut = image[y:y+h, x:x+w]

                resized = cv2.resize(cut, (100, 100))

                y_test_item = resized.mean(axis=2).flatten()

                output = model.predict([y_test_item])[0]

                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 5)
                cv2.putText(image, str(output), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 2)

        cv2.imshow("My first camera", image)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
