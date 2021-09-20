import cv2
# DOC ANH XAM LUU VAO BIEN IMAGE
image = cv2.imread("image/sample-2.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("image/sample_gray.png", image)
