import cv2
import numpy as np
from configs import MIN_CONTOUR_AREA, YOLO_CONFIDENCE, YOLO_THRESHOLD

def detect_colored_object(frame, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest)
        return (x, y, w, h), mask
    return None, mask

def detect_yolo(frame, net, output_layers, classes):
    """
    Detect objects using YOLO with OpenCV DNN.
    Returns list of (box, label, confidence).
    """
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    boxes, confidences, class_ids = [], [], []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > YOLO_CONFIDENCE:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indices = cv2.dnn.NMSBoxes(boxes, confidences, YOLO_CONFIDENCE, YOLO_THRESHOLD)
    results = []
    for i in indices:
        box = boxes[i]
        label = classes[class_ids[i]]
        confidence = confidences[i]
        results.append((box, label, confidence))
    return results