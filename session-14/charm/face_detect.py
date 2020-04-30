import cv2

cap = cv2.VideoCapture(1)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        cv2.imshow("My first camera", image)

        if len(faces) > 0:

            sorted_faces = sorted(faces, key=lambda item:item[2]*item[3])

            x, y, w, h = sorted_faces[-1]

            cut = image[y:y+h, x:x+w]

            resized = cv2.resize(cut, (300, 300))

            cv2.imshow("chopped", resized)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    elif key == ord("c"):
        cv2.imwrite("classroom.jpg", image)

cap.release()
cv2.destroyAllWindows()



