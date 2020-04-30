import cv2

cap = cv2.VideoCapture("playback.mp4")

while True:
    retval, image = cap.read()

    if retval:


        x, y, w, h = (100, 120, 150, 150)

        cut = image[y:y+h, x:x+w]

        cv2.imshow("My first camera", image)
        cv2.imshow("chopped", cut)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    elif key == ord("c"):
        cv2.imwrite("classroom.jpg", image)

cap.release()
cv2.destroyAllWindows()



