# 🏋️‍♂️ Push-Up Counter using Pose Estimation

This project is a **real-time push-up counter** that uses a webcam to track your workout, analyze your posture, and automatically count reps — all powered by **Python**, **OpenCV**, and **MediaPipe**.

## 🎯 Project Overview

Say goodbye to manual counting! This tool uses pose estimation to track your arms and upper body, calculates elbow angles, and maps that to a push-up motion using a custom percentage scale. The logic is designed to detect proper form and only count full push-ups with accurate movement.

Whether you're just exercising or exploring computer vision, this project engagingly combines both worlds.

---

## 🧠 Key Features

* **Pose Detection** using MediaPipe for real-time body landmark tracking
* **Custom Angle-to-Percentage Mapping** with a linear formula for precise motion tracking
* **Automatic Rep Counting** that only updates when a full push-up (down and up) is completed
* **Visual Feedback** including:

  * Live percentage display
  * Vertical bar showing movement progress
  * Push-up counter overlay
  * FPS meter for performance monitoring
* **Form Validation:** Prompts you to “Take your position” when pose isn’t detected clearly
* **Flip View for Mirror Effect** to better match user orientation

---

## 📦 Tech Stack

* **Language**: Python
* **Libraries**:

  * `OpenCV` – for real-time video and image processing
  * `NumPy` – numerical operations and interpolation
  * `MediaPipe` – to detect body landmarks (via custom `poseEstimationModule.py`)

---

## 💪 How It Works

1. Webcam feed is captured and resized to a consistent frame size.
2. MediaPipe detects body pose landmarks.
3. The elbow joint angles are calculated using landmark coordinates.
4. A custom linear equation converts the angle into a movement percentage.
5. If the movement reaches full depth (0%) and comes back up (100%), the counter increments by 1.
6. Real-time overlays show feedback like rep count, progress bar, and performance FPS.

---

## 🚀 Why I Built This

I wanted to explore how computer vision can be used to enhance everyday activities — and what’s more common than a push-up? This project was a great way to dive deeper into pose estimation and bring some tech into fitness routines.

---

## 📸 Example Output

> (You can add a screenshot or short demo video here!)

---

## 🛠 Future Improvements

* Add squat/lunge detection
* Track and store workout history
* Integrate voice feedback
* Use a GUI or web interface

---

## 📁 Folder Note

Make sure you have `poseEstimationModule.py` in the same folder — it's a custom wrapper around MediaPipe’s pose detection.

---

## 📌 Requirements

* Python 3.x
* OpenCV
* NumPy
* MediaPipe

Install them using pip:

```bash
pip install opencv-python mediapipe numpy
```

---

## 🧑‍💻 Run the Project

```bash
python pushUpCounter.py
```

Ensure your webcam is connected and that permissions are granted.

---

## 🙌 Contributions & Feedback

Feel free to fork, play around, or submit PRs! If you try it out, I’d love to see your version or ideas for improvement.

---
