import cv2

# Path to the image file
img_file = '/Users/bethwel/Desktop/vehicle-recognition/cars.jpg'

# Path to the car detector XML file
classifier_file = '/Users/bethwel/Desktop/vehicle-recognition/car_detector.xml'

# Load the image
img = cv2.imread(img_file)

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create the car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# Detect cars in the image
cars = car_tracker.detectMultiScale(gray_img)

# Draw rectangles and label each car
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 200), 2)
    cv2.putText(img, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 200), 2)

# Display the image with car detections
cv2.imshow('Car Recognition Software', img)

# Wait for a key press to exit
cv2.waitKey(0)

print("My Car Recognition Software")