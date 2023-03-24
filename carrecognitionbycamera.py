import cv2

webcam = cv2.VideoCapture(0)

classifier_for_cars = '/Users/bethwel/Desktop/vehicle-recognition/car_detector.xml'
classifier_for_pedestrians = '/Users/bethwel/Desktop/vehicle-recognition/haarcascade_fullbody.xml'

vehicle_detector = cv2.CascadeClassifier(classifier_for_cars)
pedestrian_detector = cv2.CascadeClassifier(classifier_for_pedestrians)

while True:
    read_successful, frame = webcam.read()
    
    if read_successful:
        black_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    else:
        break


    cars = vehicle_detector.detectMultiScale(black_white)
    pedestrians = pedestrian_detector.detectMultiScale(black_white)

    #print(cars)

    for (x,y,w,h) in cars:
     cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),5 )

    for (x,y,w,h) in pedestrians:
     cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2 )



    

    cv2.imshow('OUR CAR RECOGNITION SOFTWARE', frame)

    key=cv2.waitKey(1)

    if key==81 or key==113 or key==27 or key==8:
       break

webcam.release()
