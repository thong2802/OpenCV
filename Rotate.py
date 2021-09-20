import cv2
import imutils

image = cv2.imread("image/sample-2.png")
cv2.imshow("Anh", image)
cv2.waitKey()

# quay anh 90 do
image_rotate = imutils.rotate(image, 90)
cv2.imshow("image resize", image_rotate)
# dung ham phuc tap
# lay cao lay rong
#(h, w) = image.shape[:2]
# tinh tâm bức  ,góc quay, và mức độ
#center = (w / 2, h / 2)
#angle = 90
#scale = 1.0
# quay nguoc 90 do
#M = cv2.getRotationMatrix2D(center, angle, scale)
#rotate90 = cv2.warpAffine(image, M, (h,w))
cv2.waitKey()
cv2.destroyAllWindows()