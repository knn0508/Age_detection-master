// JavaScript for Age Prediction App

// Check if we're in production environment
const isProduction = window.location.hostname.includes('render.com') || 
                     window.location.hostname.includes('onrender.com');

// Check camera availability on page load
document.addEventListener('DOMContentLoaded', function() {
    if (isProduction) {
        showProductionNotice();
        disableCameraFeatures();
    }
});

function showProductionNotice() {
    // Add production notice to pages with camera features
    const cameraElements = document.querySelectorAll('[data-camera-required="true"]');
    if (cameraElements.length > 0) {
        const notice = document.createElement('div');
        notice.className = 'production-notice';
        notice.innerHTML = `
            <h3>🚀 Production Environment</h3>
            <p>Camera features are disabled in the cloud environment. Please use image upload functionality instead.</p>
        `;
        
        // Insert notice at the top of main content
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
            mainContent.insertBefore(notice, mainContent.firstChild);
        }
    }
}

function disableCameraFeatures() {
    // Disable real-time mode
    const realtimeCard = document.querySelector('a[href="/realtime_mode"]');
    if (realtimeCard) {
        realtimeCard.parentElement.classList.add('feature-disabled');
        realtimeCard.onclick = function(e) {
            e.preventDefault();
            alert('Real-time video streaming is not available in production environment. Please use image upload instead.');
        };
    }
    
    // Disable capture buttons
    const captureButtons = document.querySelectorAll('[data-action="capture"]');
    captureButtons.forEach(button => {
        button.disabled = true;
        button.textContent = 'Camera Not Available';
        button.onclick = function(e) {
            e.preventDefault();
            alert('Camera access is not available in production environment.');
        };
    });
    
    // Hide video feed
    const videoElements = document.querySelectorAll('img[src="/video_feed"]');
    videoElements.forEach(video => {
        video.style.display = 'none';
        const parent = video.parentElement;
        if (parent) {
            const message = document.createElement('div');
            message.className = 'camera-warning';
            message.innerHTML = '<strong>Camera Unavailable</strong>Real-time video streaming is not supported in production environment.';
            parent.appendChild(message);
        }
    });
}
