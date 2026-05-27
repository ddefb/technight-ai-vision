# FaceVibe AI Vision
### Tech Night 2026.1 Edition

FaceVibe AI Vision is a real-time emotion recognition platform designed for interactive experiences, live demonstrations, and AI showcase environments.

Built with Flask, OpenCV, TensorFlow/Keras, and Docker, the system performs facial emotion analysis directly from a live camera feed and presents the results through a modern fullscreen interface optimized for TVs, kiosks, and event displays.

This project evolved from the original FaceVibe repository into a production-ready interactive AI experience showcased at Tech Night 2026.1.

---

# Features

## Real-Time Emotion Detection

Detects and classifies facial emotions live through webcam video streams.

Supported emotions:
- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

---

## AI-Powered Inference

Uses a pre-trained TensorFlow/Keras CNN model for facial emotion classification.

---

## Fullscreen Event Interface

Custom UI inspired by the CESAR School Tech Night visual identity:
- Fullscreen immersive experience
- Glassmorphism overlays
- TV-optimized layout
- Live AI status indicators
- Event-ready visual presentation

---

## Dockerized Deployment

The application is fully containerized using Docker and Docker Compose:
- Easy deployment
- Environment isolation
- Restart recovery
- Healthcheck monitoring

---

## TV / Kiosk Optimized

Designed specifically for:
- Tech events
- Exhibition booths
- AI showcases
- Interactive installations
- Smart TV displays
- Kiosk mode presentations

---

# Tech Stack

- Flask
- OpenCV
- TensorFlow / Keras
- NumPy
- Docker
- HTML5 / CSS3

---

# Project Structure

```plaintext
facevibe/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
│
├── models/
│   └── model.h5
│
├── haarcascades/
│   └── haarcascade_frontalface_default.xml
│
├── static/
│   ├── style.css
│   └── logo_cesar.png
│
└── templates/
    └── index.html
```

---

# Running Locally

## 1. Clone the Repository

```bash
git clone git@github.com:ddefb/technight-ai-vision.git
cd technight-ai-vision
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

---

# Running with Docker

## Build Container

```bash
docker compose build
```

---

## Start Application

```bash
docker compose up
```

---

## Run in Background

```bash
docker compose up -d
```

---

# Healthcheck & Recovery

The container includes:
- Automatic restart policies
- Healthcheck monitoring
- Failure recovery support

Useful for long-running demos and event installations.

---

# Kiosk Mode (Recommended for TVs)

For fullscreen event presentation:

```bash
chromium --kiosk http://localhost:5000
```

---

# Demo Experience

The interface was redesigned for Tech Night 2026.1 with:
- CESAR School-inspired visual identity
- Large-scale TV readability
- Minimalist futuristic overlays
- Interactive AI showcase aesthetics

---

# Credits

This project was originally based on the repository: https://github.com/letsdoitbycode/FaceVibe

The project was extended and redesigned with:
- Docker infrastructure
- Event-oriented UI/UX
- Fullscreen TV presentation
- Production deployment improvements
- Healthcheck and recovery support
- Modern visual interface

---

# License

This project maintains attribution to the original repository and is intended for educational, research, and demonstration purposes.
