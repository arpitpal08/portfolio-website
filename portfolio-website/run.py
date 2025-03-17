#!/usr/bin/env python
"""
Run script for the portfolio website
"""

import os
from app import app

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs('frontend/static/images', exist_ok=True)
    os.makedirs('frontend/static/css', exist_ok=True)
    os.makedirs('frontend/static/js', exist_ok=True)
    os.makedirs('frontend/static/files', exist_ok=True)
    os.makedirs('backend/data', exist_ok=True)
    os.makedirs('ai-chatbot/data', exist_ok=True)
    os.makedirs('ai-chatbot/data/conversations', exist_ok=True)
    
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 5000))
    
    # Run the application
    app.run(host='127.0.0.1', port=port, debug=True) 