import cv2
capture = cv2.VideoCapture('rtsp://admin:william1560@192.168.128.4:554/Streaming/channels/301/') #Cámaras
# capture = cv2.VideoCapture('rtsp://administrador:william1560@192.168.128.3:554/stream1') cámara abajo
# rtsp://administrador:william1560@192.168.128.3:554/stream1

#capture = cv2.VideoCapture("rtsp://usuario:***ADMIN@192.168.12813/video")


while True:
    ret, frame = capture.read()
    cv2.imshow('captura', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()