import cv2

# doc anh den trang
image = cv2.imread("sample-2.png", cv2.IMREAD_GRAYSCALE)
#show anh
cv2.imshow("Anh", image)
# dung man hinh
cv2.waitKey()
#dong tat ca cua so lai
cv2.destroyAllWindows()

