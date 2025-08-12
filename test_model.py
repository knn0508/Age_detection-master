#!/usr/bin/env python3
"""
Model initialization test script
"""

import os
import sys

def test_model_initialization():
    """Test if InsightFace model can be initialized"""
    print("🔍 Testing AI model initialization...")
    
    try:
        print("1. Importing required packages...")
        from insightface.app import FaceAnalysis
        print("✅ Successfully imported InsightFace")
        
        print("2. Creating FaceAnalysis instance...")
        model = FaceAnalysis(name="buffalo_l")
        print("✅ FaceAnalysis instance created")
        
        print("3. Preparing model (this may take a while on first run)...")
        model.prepare(ctx_id=-1)  # Use CPU
        print("✅ Model prepared successfully")
        
        print("4. Testing model with dummy data...")
        import numpy as np
        import cv2
        
        # Create a simple test image (black image)
        test_image = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Try to detect faces (should return empty list for black image)
        faces = model.get(test_image)
        print(f"✅ Model test completed. Detected {len(faces)} faces in test image.")
        
        print("\n🎉 Model initialization successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all packages are installed: pip install -r requirements.txt")
        return False
        
    except Exception as e:
        print(f"❌ Model initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_environment():
    """Check environment and dependencies"""
    print("🔧 Checking environment...")
    
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    
    # Check if running in production
    env = os.environ.get('ENVIRONMENT', 'development')
    print(f"Environment: {env}")
    
    # Check requirements.txt packages
    try:
        import flask
        print(f"✅ Flask version: {flask.__version__}")
    except ImportError:
        print("❌ Flask not installed")
        
    try:
        import cv2
        print(f"✅ OpenCV version: {cv2.__version__}")
    except ImportError:
        print("❌ OpenCV not installed")
        
    try:
        import numpy
        print(f"✅ NumPy version: {numpy.__version__}")
    except ImportError:
        print("❌ NumPy not installed")
        
    try:
        import insightface
        print(f"✅ InsightFace available")
    except ImportError:
        print("❌ InsightFace not installed")

def main():
    print("🚀 AI Model Diagnostic Tool\n")
    
    # Test environment first
    test_environment()
    print("\n" + "="*50 + "\n")
    
    # Test model initialization
    success = test_model_initialization()
    
    print("\n" + "="*50)
    
    if success:
        print("✅ All tests passed! Your model should work in the Flask app.")
        return 0
    else:
        print("❌ Model initialization failed. Check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
