import cv2

image = cv2.imread("image/sample-2.png")
cv2.imshow("Anh", image)
cv2.waitKey()
#image_resize = cv2.resize(image, dsize=(100,200))
image_resize = cv2.resize(image, dsize = None, fx = 0.5, fy = 0.5)
cv2.imshow("image resize", image_resize)
cv2.waitKey()
cv2.destroyAllWindows()