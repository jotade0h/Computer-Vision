import cv2
cap = cv2.VideoCapture('rtsp://admin:william1560@192.168.128.4:554/Streaming/channels/301/')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()