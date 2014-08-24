#!/usr/bin/env python
#largely based on https://realpython.com/blog/python/face-recognition-with-python/
import cv, cv2
import numpy as np
import urllib2
import glob

def readImage(imgPath):
    if 'http' in imgPath:
        try:
            req = urllib2.urlopen(imgPath)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            image = cv2.imdecode(arr,-1)
        except:
            return None
    else:
        image = cv2.imread(imgPath)
    return image

def detectFaces(imgPath, cascPath):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = readImage(imgPath)
    if image is None:
        print "Error reading %s" % imgPath
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    print "Found %d faces in %s!" % (len(faces), imgPath)
    return len(faces)

def facesAreSimilar(imgPath1, imgPath2):
    image1 = cv2.cvtColor(readImage(imgPath1), cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(readImage(imgPath2), cv2.COLOR_BGR2GRAY)
    hist1 = cv2.calcHist([image1.astype('float32')], channels=[0], mask=None, histSize=[64], ranges=[0,64])
    hist2 = cv2.calcHist([image2.astype('float32')], channels=[0], mask=None, histSize=[64], ranges=[0,64])

    similarity = cv2.compareHist(hist1, hist2, method = cv.CV_COMP_CORREL)
    print "Similarity score %s vs %s: %f.2" % (imgPath1, imgPath2, similarity)
    return similarity > 0.98

if __name__ == '__main__':
    cascPath = 'haarcascade_frontalface_default.xml'
    imgPath = 'images/*.jpg'
    imgFiles = glob.glob(imgPath)
    for imgFilePath in imgFiles:
        detectFaces(imgFilePath, cascPath)
        for imgFilePath2 in imgFiles:
            facesAreSimilar(imgFilePath, imgFilePath2)
        
    detectFaces('http://answers.opencv.org/upfiles/logo_2.png', cascPath)
