

This project implements a motion detection alarm system using Python. The system uses your computer's webcam to detect motion and triggers an alarm when movement is detected.

## Features
- **Motion Detection**: Identifies movement in the camera's view.
- **Sound Alarm**: Plays a beep sound upon detecting motion.
- **Alert Logging**: Logs every motion detection event with a timestamp.
- **Graphical User Interface**: Easy-to-use GUI built with `tkinter`.

## How It Works
1. The system accesses the webcam feed using `OpenCV`.
2. Background subtraction is used to detect motion.
3. When motion is detected, the following actions occur:
   - A rectangle is drawn around the moving object.
   - An alarm sound is played.
   - The event is logged in a text file (`alerts_log.txt`).
4. Users can start or stop the camera feed via the GUI.

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `opencv-python`
  - `numpy`
  - `pillow`
  - `tkinter` (usually included with Python)

### Install Dependencies
Run the following command to install the required packages:
```bash
pip install opencv-python numpy pillow
```

## Usage
1. Run the script:
   ```bash
   camera alert.py
   ```
2. Use the GUI to start or stop the camera.
3. Check the `alerts_log.txt` file for logged alerts.

## Logs
- Alerts are saved in `alerts_log.txt` with timestamps.

## Contribution
Feel free to fork the repository and make improvements. Submit a pull request with your changes.
