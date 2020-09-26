import numpy as np
import cv2
from keras.models import load_model
#define preProcessing
def preProcessing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img
#load model
model = load_model('classification_model.h5')

width = 640
height = 480
threshold = 0.65
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
while True:
    success, frame = cap.read()
    img = np.asarray(frame)
    img = cv2.resize(img, (28, 28))
    img = preProcessing(img)
    img = img.reshape(1,28, 28, 1)

    #predict
    class_index = int(model.predict_classes(img))
    print(class_index)
    predictions = model.predict(img)
    propval = np.max(predictions)
    print(str(class_index) + "   " + str(propval))
    if propval >=threshold:
        cv2.putText(frame, str(class_index)+"   "+str(propval), (50,50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
