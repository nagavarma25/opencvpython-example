import cv2


img = cv2.imread('penguins.jpeg',1)


# resized = cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))
# cv2.imshow('penguins',resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('group.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                      minNeighbors=5)

print(type(faces))
print(faces)

