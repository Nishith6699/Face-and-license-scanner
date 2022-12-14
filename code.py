import cv2
import os
import numpy as np
import winsound
a = 0
height = 500
width = 500
try:
    os.remove("C:/Users/MANAV/PycharmProjects/pythonProject/live-face.jpg")
except:pass
cap = cv2.VideoCapture(1)
for i in range(0, 2):
    ret, img = cap.read()
    cv2.imshow('lic', img)
    newpath = "license dataset/"+'L'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    cv2.imwrite("license dataset/"+'L'+"/"+'L'+"_"+str(i)+".jpg", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
# test image
image = cv2.imread('license.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
# data1 image
names = []
paths = []
minvalue = 2
for users in os.listdir("C:/Users/MANAV/PycharmProjects/pythonProject/license dataset/"):
    names.append(users)
for name in names:
    for image in os.listdir("C:/Users/MANAV/PycharmProjects/pythonProject/license dataset/{}".format(name)):
        pathstring = os.path.join("C:/Users/MANAV/PycharmProjects/pythonProject/license dataset/{}".format(name), image)
        paths.append(pathstring)
for i in range(0, 1):
    frame = cv2.imread(paths[i])
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, res = cv2.threshold(th3, minvalue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imwrite("license dataset/F/"+str(i)+".jpg", res)
image = cv2.imread('C:/Users/MANAV/PycharmProjects/pythonProject/license dataset/L/L_0.jpg')
gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
# data2 image
image = cv2.imread('test.jpg')
gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
c1, c2 = 0, 0
# chi squared distance of data1 and test
a = len(histogram)
b = len(histogram1)
eps = 1e-10
d1 = 0.5 * np.sum(((a - b) ** 2) / (a + b + eps))
# Euclidean Distance between data1 and test
i = 0
while i < len(histogram) and i < len(histogram1):
    c1 += (histogram[i] - histogram1[i]) ** 2
    i += 1
c1 = c1 ** (1 / 2)
# chi squared distance of data2 and test
c = len(histogram2)
d2 = 0.5 * np.sum(((a - c) ** 2) / (a + c + eps))
# Euclidean Distance between data2 and test
i = 0
while i < len(histogram) and i < len(histogram2):
    c2 += (histogram[i] - histogram2[i]) ** 2
    i += 1
c2 = c2 ** (1 / 2)

if c1 < c2 :
#if s1 > s2:
    #print("success go to next step ")
    cap = cv2.VideoCapture(1)
    for i in range(0, 5):
        ret, img = cap.read()
        cv2.imshow('web face', img)
        newpath = "Face dataset/" + 'F'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        cv2.imwrite("face dataset/" + 'F' + "/" + 'F' + "_" + str(i) + ".jpg", img)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
    # test image
    image = cv2.imread('face.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = image[y:y + h, x:x + w]
        cv2.imwrite('face1.jpg', faces)
    img1 = cv2.imread('face1.jpg')
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([img1], [0], None, [256], [0, 256])

    # data1 image
    names = []
    paths = []
    minvalue = 2
    for users in os.listdir("C:/Users/MANAV/PycharmProjects/pythonProject/Face dataset/"):
        names.append(users)
    for name in names:
        for image in os.listdir("C:/Users/MANAV/PycharmProjects/pythonProject/Face dataset/{}".format(name)):
            pathstring = os.path.join("C:/Users/MANAV/PycharmProjects/pythonProject/Face dataset/{}".format(name),
                                      image)
            paths.append(pathstring)
    for i in range(0, 4):
        frame = cv2.imread(paths[i])
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 2)
        th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        ret, res = cv2.threshold(th3, minvalue, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        cv2.imwrite("face processed/F/" + str(i) + ".jpg", res)
    image = cv2.imread('C:/Users/MANAV/PycharmProjects/pythonProject/Face dataset/F/F_0.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = image[y:y + h, x:x + w]
        cv2.imwrite('live-face.jpg', faces)
    img2 = cv2.imread('live-face.jpg')
    try:
      gray_image1 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
      histogram1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

      # data2 image
      image = cv2.imread('test.jpg')
      gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      histogram2 = cv2.calcHist([image], [0], None, [256], [0, 256])

      c1, c2 = 0, 0
      # chi squared distance of data1 and test
      a = len(histogram)
      b = len(histogram1)
      eps = 1e-10
      i = 0
      while i < a and i < b:
        d1 += 0.5 * np.sum(((histogram[i] - histogram1[i]) ** 2) / (histogram[i] + histogram1[i] + eps))
        i += 1
      # Euclidean Distance between data1 and test
      i = 0
      while i < len(histogram) and i < len(histogram1):
           c1 += (histogram[i] - histogram1[i]) ** 2
           i += 1
      c1 = c1 ** (1 / 2)
      # chi squared distance of data2 and data1
      c = len(histogram2)
      i = 0
      while i < b and i < c:
        d2 += 0.5 * np.sum(((histogram1[i] - histogram2[i]) ** 2) / (histogram[i] + histogram2[i] + eps))
        i += 1
       # Euclidean Distance between data2 and data1
      i = 0
      while i < len(histogram1) and i < len(histogram2):
           c2 += (histogram1[i] - histogram2[i]) ** 2
           i += 1
      c2 = c2 ** (1 / 2)
      a = 1

      if d1 < d2 and c1 < c2:
         print("success go to next step ")
      else:
          print("face not matched")
          frequency = 1000
          duration = 1000
          winsound.Beep(frequency, duration)
    except:pass
    if(a!=1):
      print("face not detected")
      frequency = 1000
      duration = 1000
      winsound.Beep(frequency, duration)
else:
    print("licence not matched")
    frequency = 1000
    duration = 1000
    winsound.Beep(frequency, duration)
    #os.remove("C:/Users/MANAV/PycharmProjects/pythonProject/live-face.jpg")
