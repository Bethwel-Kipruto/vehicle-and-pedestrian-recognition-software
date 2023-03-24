import cv2
#import numpy as np

#our image
img_file = '/Users/bethwel/Desktop/cars.jpg'



#our pre trained car spotting software(the car_detector.xml file in this project )--write the path of the file if its name doesn't work
classifier_file = '/Users/bethwel/Desktop/vehicle-recognition/car_detector.xml'

#turn our image into the opencv format...this is the image we have on line 4 (allowing the cv2 to read our image)
img = cv2.imread(img_file)

#use the 'convert color function' ...turn my images to black and white ....for the haar cascade to read the image as black and white...IN THIS CASE FROM THE BlueGreenRed scale to gray
black_white_only = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



#create your car classifier(whatever is going to classify a car is in your image or view of your camera)....in this case it's the data in our xml file
car_tracker = cv2.CascadeClassifier(classifier_file)

#now we are going to detect a car in our image (using our classifier)--the function 'detectMultiScale' simply means our program should detect a car of any size 
cars = car_tracker.detectMultiScale(black_white_only)



#this outputs coordinates of the cars in our image in form of arrays,we will use the array data to draw rectangles around the cars
#print(cars)

#draw a rectangle to enclose the car and mark the area around it....for each  of the 4 coordinates to be assigned into x,y,w,h
for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,200),2) #cv2.rectangle(yourimg,(topleft),(topright),(blue,green,red),thickness of line)


cv2.imshow('OUR CAR RECOGNITION SOFTWARE',img)




#simply telling our program to not close as soon as it executes the program
cv2.waitKey()






print("My Car Recognition Software")