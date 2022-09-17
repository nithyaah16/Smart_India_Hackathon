import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("frame728.jpg",)  #giving the frame as input
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #converting to grayscale

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,
minNeighbors = 5)   #applying the algorithm


for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (50, 0, 0), 4)  
    #defining a box around the face region detected 

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/4))) #resizing

cv2.imshow("Face detection", resized)
cv2.imwrite("frame106_facedetected.jpg", resized)  #saving the images
cv2.waitKey(0)
cv2.destroyAllWindows()