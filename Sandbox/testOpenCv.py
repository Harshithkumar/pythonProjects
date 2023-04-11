import cv2

print("Its the beginning")
print("Your OpenCV version is: " + cv2.__version__)

# read an image in colour mode



img = cv2.imread("/Users/hakumar/PycharmProjects/Experiments/Sandbox/Assets/tiger.jpg", 0)

# display the image in a window
#cv2.namedWindow('window', cv2.WINDOW_NORMAL)

cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




'''
#A frame in video output:
earth = cv2.VideoCapture("/Users/hakumar/PycharmProjects/Experiments/Sandbox/Assets/Earth_2.mp4")
while earth.isOpened():
    ret, frame = earth.read()
    if not ret:
        break
   # cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.imshow('Window', frame)
    cv2.waitKey(1)
    print(earth.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(earth.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(earth.get(cv2.CAP_PROP_FOURCC))
    print(earth.get(cv2.CAP_PROP_FRAME_COUNT))
earth.release()
cv2.destroyAllWindows()
'''
# display the image in a window

img = cv2.imread("/Users/hakumar/PycharmProjects/Experiments/Sandbox/Assets/tiger.jpg", 1)
print(img.shape)

# arguments: image, start, end, colour, thickness

img = cv2.line(img, (200,400), (200, 600), (0,255,0), 10 )
img = cv2.circle(img, (2220,700), 450, (255,0,0), 5)
cv2.imshow('tiger', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
