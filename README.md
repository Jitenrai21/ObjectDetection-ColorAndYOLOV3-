# 🎨📸 ObjectTrackingApp-ByColor

A Python-based object detection system for identifying colored or specific objects via webcam.

---

## 👋 Welcome

Welcome to **ObjectTrackingApp-ByColor**!  
This Python project lets you detect objects using:

- **Color detection** (pink, light blue, yellow, green, white, orange)  
- **Specific object classes** (e.g., bottle, person) via **YOLOv3 or YOLOv3-Tiny**

Built with **OpenCV** and **YOLO**, this app provides:

- Real-time detection  
- Mode switching (color ↔ YOLO)  
- Bounding boxes and optional HSV masks  

---

## 🌟 Features

### 🎨 Color Detection

Identify objects of the following colors in real-time:

| Key | Color        | Emoji       |
|-----|--------------|-------------|
| `p` | Pink         | 💗          |
| `b` | Light Blue   | 💙          |
| `y` | Yellow       | 💛          |
| `g` | Green        | 💚          |
| `w` | White        | 🤍          |
| `o` | Orange       | 🧡          |

### 🤖 YOLO Object Detection

Press `d` to switch to **DNN (YOLO)** mode to detect specific object classes like `bottle`, `person`, etc.

### 💡 Real-time Feedback

- Bounding box with labels (e.g., `"Pink Object"` or `"Bottle: 0.95"`)  
- Current mode and selection display  
- On-screen instructions for key controls  
- Optional HSV mask window (can be toggled)

---

## 📂 Project Structure

```
ColorObjectDetectorApp/
├── env/                    # 🌐 Virtual environment
├── tracking/               # 🛠️ Detection scripts
│   ├── detector.py         # 🎨 Object detection logic
│   └── utils.py            # 🖼️ Visualization utilities
├── tests/                  # 🧪 Unit tests
│   ├── config.py           # ⚙️ Test configuration
│   ├── test_detector.py    # 🧪 Detection tests
├── configs.py              # ⚙️ Main configuration
├── main.py                 # 🚀 Main application
├── requirements.txt        # 📋 Dependencies
├── ProjectStructure.txt    # 📄 Project structure documentation
```

---

## 🛠️ Getting Started

### 📋 Prerequisites

- Python 3.8+  
- Webcam  
- YOLOv3 model files (downloaded manually)

### 🧱 Required Packages

- `opencv-python`  
- `numpy`  

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jitenrai21/ObjectTrackingApp-ByColor-.git
cd ObjectTrackingApp-ByColor
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
```

**Activate Virtual Environment**

*Windows:*
```bash
.\env\Scripts\activate
```

*macOS/Linux:*
```bash
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download YOLO Model Files

Download the following files and place them in the `models/` directory:

- [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)  
- [yolov3.cfg](https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg)  
- [yolov3-tiny.weights](https://pjreddie.com/media/files/yolov3-tiny.weights)  
- [yolov3-tiny.cfg](https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg)  
- [coco.names](https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names)

> ⚠️ **Note:** Ensure the file names match exactly as referenced in `configs.py` (e.g., `models/coco.names`, not `coco.names.txt`)

---

## 🚀 Running the Application

```bash
python main.py
```

---

## 🎮 How to Use

- Point your webcam at an object (e.g., a pink cloth or a bottle)  
- Use the following keys to control the app:

| Key | Action                         |
|-----|--------------------------------|
| `p` | Detect Pink objects            |
| `b` | Detect Light Blue objects      |
| `y` | Detect Yellow objects          |
| `g` | Detect Green objects           |
| `w` | Detect White objects           |
| `o` | Detect Orange objects          |
| `c` | Switch to Color Detection Mode |
| `d` | Switch to YOLO DNN Mode        |
| `q` | Quit the application           |

---

## 🧩 Customization

### Add New Colors

- Modify `COLOR_RANGES` in `configs.py`  
- Update key bindings in `main.py`

### Adjust YOLO Parameters

- Change `YOLO_CONFIDENCE` and `YOLO_THRESHOLD` in `configs.py`

### Add Object Classes

- Edit `coco.names` or replace with a custom YOLO-trained model

### Toggle HSV Mask Display

- Set `SHOW_MASK = False` in `configs.py`

### Use YOLOv3-Tiny for Faster Detection

- Update `YOLO_WEIGHTS` and `YOLO_CFG` in `configs.py` with:
  - `yolov3-tiny.weights`
  - `yolov3-tiny.cfg`

---

## 🐞 Troubleshooting

### Webcam Not Working?

- Ensure it’s connected and functional  
- Change `CAMERA_INDEX` in `configs.py` (try 0, 1, 2...)

### YOLO Not Detecting?

- Ensure model files exist in the `models/` directory  
- Check names and paths in `configs.py`  
- Lower `YOLO_CONFIDENCE` to e.g., `0.3`  
- Try using `yolov3-tiny` instead  

### Colors Not Detected?

- Use bright, solid-colored objects  
- Adjust HSV ranges in `configs.py`  
- Improve lighting

### Text Overlap?

- Change text position or font size in `main.py` (e.g., update coordinates like `(10, 90)` → `(10, 100)`)

### Large Files in Git?

If you accidentally committed `models/`:

```bash
git rm -r --cached models/
git commit -m "Remove models/ from Git tracking"
git push origin main
```

---

## 🤝 Contributing

Want to improve this app? Here's how:

1. **Fork the repository**
2. **Create a new branch**  
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**  
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to GitHub**  
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** 🚀

---

## 🙏 Acknowledgments

- [OpenCV](https://opencv.org/) – Real-time computer vision and DNN support  
- [YOLO (You Only Look Once)](https://pjreddie.com/darknet/yolo/) – Object detection framework  
- **You** – For checking out this project ❤️

---

**Built with passion by Jiten Rai**  
**Happy Detecting! 🎉**
