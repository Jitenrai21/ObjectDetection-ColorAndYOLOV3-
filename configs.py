# config.py
CAMERA_INDEX = 0  # Use 0 for default webcam

# HSV Color Ranges
COLOR_RANGES = {
    'pink': {
        'LOWER_HSV': [(150, 50, 100)],
        'UPPER_HSV': [(180, 150, 255)]
    },
    'blue': {
        'LOWER_HSV': [(100, 50, 150)],
        'UPPER_HSV': [(120, 150, 255)]
    },
    'yellow': {
        'LOWER_HSV': [(20, 100, 100)],
        'UPPER_HSV': [(40, 255, 255)]
    },
    'green': {
        'LOWER_HSV': [(40, 100, 100)],
        'UPPER_HSV': [(80, 255, 255)]
    },
    'white': {
        'LOWER_HSV': [(0, 0, 200)],
        'UPPER_HSV': [(180, 50, 255)]
    },
    'orange': {
        'LOWER_HSV': [(10, 100, 100)],
        'UPPER_HSV': [(20, 255, 255)]
    }
}

# Default color
DEFAULT_COLOR = 'yellow'
LOWER_HSV = COLOR_RANGES[DEFAULT_COLOR]['LOWER_HSV'][0]
UPPER_HSV = COLOR_RANGES[DEFAULT_COLOR]['UPPER_HSV'][0]

# Window Settings
SHOW_MASK = True
WINDOW_NAME = "Object Tracker"

# Detection Settings
MIN_CONTOUR_AREA = 500

# YOLO Configuration
YOLO_WEIGHTS = "models/yolov3.weights" # pre-trained model weights
YOLO_CFG = "models/yolov3.cfg" # network architecture
# YOLO_WEIGHTS = 'models/yolov3-tiny.weights'
# YOLO_CFG = 'models/yolov3-tiny.cfg'
YOLO_NAMES = "models/coco.names.txt" # list of COCO dataset classes, e.g., person, car, bottle
YOLO_CONFIDENCE = 0.5  # Confidence threshold
YOLO_THRESHOLD = 0.3   # NMS threshold