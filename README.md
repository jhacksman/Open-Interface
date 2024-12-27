# Molmo Browser Test

A local browser-based test mode for Molmo model that enables UI element detection and coordinate extraction.

## Features

- Local deployment (no external APIs)
- Screenshot analysis for UI elements
- Coordinate and bounding box detection
- Pink dot visualization
- JSON coordinate output

## Requirements

- Python 3.8+
- 10GB+ VRAM for Molmo model
- FastAPI
- OpenCV

## Setup

1. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Run the server:
```bash
uvicorn app.main:app --reload
```

4. Open frontend/index.html in your browser

## Usage

1. Upload a screenshot or capture browser window
2. Get coordinates and bounding boxes for UI elements
3. View visualization with pink dots

## Architecture

- Backend: FastAPI service with Molmo integration
- Frontend: Simple HTML/JS interface
- Local processing: All computation done on local machine or LAN
