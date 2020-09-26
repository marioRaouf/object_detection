this is a project about object detection and object classification in real time.

	the real time classification steps is very simple:
1-train your classification model.                                                          
2-capture the frames from a video or from web cam and feed it to the model using opencv python library.
3-use open cv to add text to the frame with it's label and it's accuracy


	the detection in one image:
1-download the yolov3 or any version you like
2-add the weights and cfg files in weights and cfg folders.
3-add the coco.names and the image containing the objects you want to classify in the same directory as yolo_object_detection_in_an_image.py 
3-run yolo_object_detection_in_an_image.py

	the real time and video deteciton:
work the same way as detection in one image but the only difference is we are not loading the image from a file but read the frame from a video or web cam.
