import cv2
import numpy as np
import os

cap = cv2.VideoCapture(1)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

name = input("Enter you name : ")
count = int(input("Enter number of pics : "))
images = []

while True:
    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        cv2.imshow("My first camera", image)

        if len(faces) > 0:

            sorted_faces = sorted(faces, key=lambda item:item[2]*item[3])

            x, y, w, h = sorted_faces[-1]
            cut = image[y:y+h, x:x+w]
            resized = cv2.resize(cut, (100, 100))
            cv2.imshow("chopped", resized)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    elif key == ord("c"):
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        images.append(gray.flatten())
        print(count)
        count -= 1
        if count == 0:
            break

cap.release()
cv2.destroyAllWindows()

X = np.array(images)
y = np.full((X.shape[0], 1), name)

data = np.hstack([y, X])


if os.path.exists("faces.npy"):
    old = np.load("faces.npy")
    data = np.vstack([old, data])

np.save("faces.npy", data)



