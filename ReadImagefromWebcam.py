import cv2
camera_id = 'sample.avi'
# mo camera
cap = cv2.VideoCapture(camera_id)
#doc anh tu webcam
while(True):
    #doc tung fram cua video
    ret, frame = cap.read()
    #hien anh
    cv2.imshow("Anh", frame)

    # kiem tra neu bam q thi thoat
    if cv2.waitKey() & 0xFF == ord ('q'):
        break
#giai phong camera
cap.release()
cv2.destroyAllWindows()