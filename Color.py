import cv2

image = cv2.imread("image/sample-2.png")
cv2.imshow("Anh", image)
cv2.waitKey()
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Anh gray", image_gray)
cv2.waitKey()
cv2.destroyAllWindows()


