#!/usr/bin/env python3
"""
Test script to verify deployment configuration
"""

import os
import sys
import subprocess

def test_requirements():
    """Test if requirements.txt exists and has basic structure"""
    print("Testing requirements.txt...")
    try:
        if os.path.exists('requirements.txt'):
            with open('requirements.txt', 'r') as f:
                content = f.read()
                required_packages = ['Flask', 'numpy', 'opencv-python', 'insightface', 'gunicorn']
                missing_packages = []
                
                for package in required_packages:
                    if package.lower() not in content.lower():
                        missing_packages.append(package)
                
                if missing_packages:
                    print(f"❌ Missing required packages: {missing_packages}")
                    return False
                else:
                    print("✅ All required packages are listed in requirements.txt")
                    return True
        else:
            print("❌ requirements.txt file not found")
            return False
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def test_app_import():
    """Test if the Flask app can be imported"""
    print("Testing Flask app import...")
    try:
        import app
        print("✅ Flask app imports successfully")
        
        # Test model initialization
        if hasattr(app, 'initialize_model'):
            print("✅ Model initialization function found")
        else:
            print("❌ Model initialization function not found")
            
        # Test environment variable handling
        os.environ['ENVIRONMENT'] = 'production'
        
        # Re-import to get updated FACES_DB_FILE
        import importlib
        importlib.reload(app)
        
        if app.FACES_DB_FILE.startswith('/opt/render'):
            print("✅ Production path configuration works")
        else:
            print("❌ Production path not configured correctly")
            print(f"Current path: {app.FACES_DB_FILE}")
            
        # Reset environment
        if 'ENVIRONMENT' in os.environ:
            del os.environ['ENVIRONMENT']
            
    except Exception as e:
        print(f"❌ Error importing Flask app: {e}")
        return False
    return True

def test_gunicorn_config():
    """Test Gunicorn configuration"""
    print("Testing Gunicorn configuration...")
    try:
        if os.path.exists('gunicorn.conf.py'):
            print("✅ Gunicorn configuration file exists")
            
            # Basic syntax check
            with open('gunicorn.conf.py', 'r') as f:
                content = f.read()
                if 'bind' in content and 'workers' in content:
                    print("✅ Gunicorn config has basic settings")
                else:
                    print("❌ Gunicorn config missing basic settings")
                    return False
        else:
            print("❌ gunicorn.conf.py missing")
            return False
    except Exception as e:
        print(f"❌ Error with Gunicorn config: {e}")
        return False
    return True

def test_static_files():
    """Test static files exist"""
    print("Testing static files...")
    static_files = ['static/app.css', 'static/app.js']
    for file_path in static_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            return False
    return True

def test_templates():
    """Test template files exist"""
    print("Testing template files...")
    template_files = [
        'templates/index.html',
        'templates/capture_mode.html', 
        'templates/browser_camera.html',
        'templates/realtime_mode.html',
        'templates/learned_faces.html'
    ]
    for file_path in template_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            return False
    return True

def test_render_config():
    """Test Render deployment configuration"""
    print("Testing Render configuration...")
    if os.path.exists('render.yaml'):
        print("✅ render.yaml exists")
        
        # Read and check basic structure
        try:
            with open('render.yaml', 'r') as f:
                content = f.read()
                if 'buildCommand:' in content and 'startCommand:' in content:
                    print("✅ render.yaml has required commands")
                else:
                    print("❌ render.yaml missing required commands")
                    return False
        except Exception as e:
            print(f"❌ Error reading render.yaml: {e}")
            return False
    else:
        print("❌ render.yaml missing")
        return False
    return True

def main():
    """Run all tests"""
    print("🚀 Running deployment configuration tests...\n")
    
    tests = [
        test_render_config,
        test_static_files,
        test_templates,
        test_gunicorn_config,
        test_app_import,
        test_requirements,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # Empty line between tests
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your app is ready for Render deployment.")
        return 0
    else:
        print("❌ Some tests failed. Please fix the issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
