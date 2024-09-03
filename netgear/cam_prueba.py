from ultralytics import YOLO
import cv2
import cvzone

cap=cv2.VideoCapture('rtsp://admin:william1560@192.168.128.4:554/Streaming/channels/301/')


while True:
    success, img= cap.read()
    cv2.imshow('Image', img)
    cv2.waitKey