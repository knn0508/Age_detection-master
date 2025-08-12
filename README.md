# Age Detection Web Applica├── templates/
    ├── index.html        # Main page
    ├── capture_mode.html # Image upload mode
    ├── browser_camera.html# Browser camera capture
    ├── realtime_mode.html# Real-time video mode
    └── learned_faces.html# Face management page

A Flask-based web application that performs real-time age detection using InsightFace models. The app supports both real-time video streaming and static image analysis with face learning capabilities.

## Features

- **Browser Camera**: Use your device's camera through web browser (works everywhere)
- **Real-time Server Streaming**: Server-side video processing (local environment only)
- **Image Upload**: Upload and analyze static images
- **Face Learning**: Recognizes and remembers faces across sessions
- **Persistent Storage**: Learned faces are saved to disk
- **Web Interface**: User-friendly HTML interface with multiple modes
- **Production Ready**: Optimized for cloud deployment on Render

## Project Structure

```
├── app.py                 # Main Flask application
├── script.py              # Standalone script for single image detection
├── script2.py             # Standalone script for real-time video detection
├── requirements.txt       # Python dependencies
├── gunicorn.conf.py       # Gunicorn configuration for production
├── render.yaml            # Render deployment configuration
├── learned_faces.pkl      # Face embeddings storage (created at runtime)
├── static/
│   ├── app.css           # Additional styles
│   └── app.js            # JavaScript for production environment handling
└── templates/
    ├── index.html        # Main page
    ├── capture_mode.html # Image upload mode
    ├── realtime_mode.html# Real-time video mode
    └── learned_faces.html# Face management page
```

## Local Development

### Prerequisites

- Python 3.8+
- Webcam (for real-time features)
- Git

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Age_detection-master
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

### Running Standalone Scripts

**Single Image Detection:**
```bash
python script.py
```

**Real-time Video Detection:**
```bash
python script2.py
```

## Production Deployment (Render)

### Prerequisites

- Render account (https://render.com)
- GitHub repository with your code

### Deployment Steps

1. **Push your code to GitHub**

2. **Create a new Web Service on Render:**
   - Connect your GitHub repository
   - Choose the branch (usually `main`)
   - Render will automatically detect the `render.yaml` configuration

3. **Environment Variables (automatically set):**
   - `ENVIRONMENT=production`
   - `PYTHON_VERSION=3.11.9`
   - `WEB_CONCURRENCY=1`

4. **Deployment Configuration (already included):**
   - Build Command: `pip install --upgrade pip && pip install -r requirements.txt`
   - Start Command: `gunicorn --config gunicorn.conf.py app:app`
   - Persistent Disk: 1GB mounted at `/opt/render/project/src/data`

### Production Limitations

- **No Camera Access**: Real-time video streaming is disabled in production
- **Image Upload Only**: Use the capture mode with image upload functionality
- **Single Worker**: Configured for model consistency

## Features by Environment

### Local Development
✅ Browser camera (device camera through web browser)
✅ Real-time video streaming (server-side webcam)
✅ Server webcam capture
✅ Image upload
✅ Face learning
✅ Persistent storage

### Production (Render)
✅ Browser camera (device camera through web browser) - **NEW!**
❌ Real-time video streaming (no server camera access)
❌ Server webcam capture (no server camera access)  
✅ Image upload
✅ Face learning
✅ Persistent storage (disk mount)

## API Endpoints

- `GET /` - Main page
- `GET /capture_mode` - Image upload mode
- `GET /browser_camera` - Browser camera capture mode
- `GET /realtime_mode` - Real-time video mode
- `GET /learned_faces` - Face management page
- `POST /upload_image` - Upload and analyze image
- `POST /capture_image` - Capture from webcam (local only)
- `GET /video_feed` - Video stream (local only)
- `GET /api/learned_faces` - Get learned faces data
- `POST /api/reset_learned_faces` - Reset all learned faces
- `POST /api/rename_person` - Rename a person
- `GET /api/model_status` - Check model status

## Technology Stack

- **Backend**: Flask, OpenCV, InsightFace, scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/ML**: InsightFace (Buffalo_L model), face embeddings
- **Production**: Gunicorn, Render platform
- **Storage**: Pickle files, persistent disk

## Configuration

### Environment Variables

- `ENVIRONMENT`: Set to 'production' for Render deployment
- `PORT`: Server port (default: 5000)
- `PYTHON_VERSION`: Python version (3.11.9)
- `WEB_CONCURRENCY`: Number of workers (1 for model consistency)

### Model Configuration

- **Model**: InsightFace Buffalo_L
- **CPU Mode**: Optimized for cloud deployment
- **Similarity Threshold**: 0.6 for face recognition
- **Frame Processing**: Every 3rd frame for performance

## Troubleshooting

### Common Issues

1. **Model Loading Errors**:
   - Ensure all dependencies are installed
   - Check Python version compatibility
   - Verify memory availability

2. **Camera Access Issues**:
   - Check camera permissions
   - Try different camera indices (0, 1, 2, 3)
   - Camera features are disabled in production

3. **Face Recognition Issues**:
   - Ensure good lighting conditions
   - Face should be clearly visible
   - Adjust similarity threshold if needed

4. **Storage Issues**:
   - Check disk permissions
   - Verify persistent storage mount
   - Monitor disk usage

### Logs

Monitor application logs for debugging:
- Local: Check terminal output
- Render: Use Render dashboard logs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally and in production environment
5. Submit a pull request

## License

This project is open source and available under the MIT License.
