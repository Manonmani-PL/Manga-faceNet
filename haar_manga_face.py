import cv2
import sys
import os.path
#filename is the picture
def detect(filename, cascade_file = "/home/user/PycharmProjects/manga_face/lbpcascade_animeface.xml"):
#checking whether that xml exist
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    #reading the image
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    #converting the image to gray scale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #equalizing the histogram to improve the contrast
    gray = cv2.equalizeHist(gray)
    #detecting the face
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    #taking the top bottom left right from the list of face
    for (x, y, w, h) in faces:
        #drawing bounding box
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #popping  a window of detecting faces
    cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)
    #saving the same
    cv2.imwrite("/home/user/PycharmProjects/manga_face/jing.jpg", image)
#check for passing arguments
if len(sys.argv) != 2:
     sys.stderr.write("usage: detect.py <filename>\n")
     sys.exit(-1)
#passing image to the function
detect(sys.argv[1])
