# Face Anonymizer: Real-time Face Blurring using OpenCV and MediaPipe
## Overview
The Face Anonymizer is a small Python project that utilizes OpenCV and MediaPipe to process live video feeds and blur human faces that are closer than 2 meters. Additionally, it can differentiate between actual humans and photographs or images of humans shown in the video.

## Features
**Real-time** face detection and tracking.
Dynamic face blurring for privacy protection.
Robust handling of varying face orientations and lighting conditions.
Human vs. photograph/image differentiation.
## Installation
### Clone this repository:
```
git clone https://github.com/yourusername/face-anonymizer.git

cd face-anonymizer
```
### Install the required dependencies:
```
pip install -r requirements.txt

```
### Usage
Run the main.py script:
python main.py



### Notes
Ensure that your camera is properly calibrated for accurate distance measurements.
Experiment with different blurring techniques (e.g., Gaussian blur, pixelation) for better results.
You can select the source of video input at 
```
cv2.VideoCapture(0)

```
0- The default Webcam

1,2...-for other webcams

'address' - adress of video for pre-recorded video 
### Credits
This project was inspired by the need for privacy in public spaces.
Thanks to the **OpenCV** and **MediaPipe** communities for their excellent libraries.
