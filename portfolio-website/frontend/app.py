from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import requests
import os
import json
from functools import wraps
import logging
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'arpit-portfolio-secret-key')

# Backend API URL
BACKEND_API_URL = os.environ.get('BACKEND_API_URL', 'http://localhost:8080/api')

# Make datetime.now available to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}

# Check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    """Render the homepage"""
    profile_data = {}
    skills_data = []
    error_message = None
    
    try:
        # Fetch basic profile data
        try:
            profile_response = requests.get(f"{BACKEND_API_URL}/profile", timeout=2)
            if profile_response.status_code == 200:
                profile_data = profile_response.json()
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for profile data")
        
        # Fetch skills data
        try:
            skills_response = requests.get(f"{BACKEND_API_URL}/skills", timeout=2)
            if skills_response.status_code == 200:
                skills_data = skills_response.json()
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for skills data")
        
        # Use static data if API is unavailable
        if not profile_data:
            profile_data = {
                "name": "Arpit Pal",
                "title": "Full Stack Developer",
                "summary": "Experienced developer with a passion for creating elegant solutions"
            }
            
        return render_template('index.html', 
                              profile=profile_data,
                              skills=skills_data,
                              error=error_message)
    except Exception as e:
        logger.error(f"Error fetching data for homepage: {str(e)}")
        return render_template('index.html', 
                                profile={"name": "Arpit Pal", "title": "Full Stack Developer"},
                                skills=[],
                                error="Unable to load data. Please try again later.")

@app.route('/about')
def about():
    """Render the about page"""
    about_data = {}
    error_message = None
    
    try:
        # Fetch about data
        try:
            about_response = requests.get(f"{BACKEND_API_URL}/about", timeout=2)
            if about_response.status_code == 200:
                about_data = about_response.json()
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for about data")
            
        # Use static data if API is unavailable
        if not about_data:
            about_data = {
                "bio": "Full Stack Developer with expertise in modern web technologies",
                "education": []
            }
        
        return render_template('about.html', about=about_data, error=error_message)
    except Exception as e:
        logger.error(f"Error fetching data for about page: {str(e)}")
        return render_template('about.html', about={}, error="Unable to load data. Please try again later.")

@app.route('/skills')
def skills():
    """Render the skills page"""
    skills_data = []
    error_message = None
    
    try:
        # Fetch skills data
        try:
            skills_response = requests.get(f"{BACKEND_API_URL}/skills", timeout=2)
            if skills_response.status_code == 200:
                skills_data = skills_response.json()
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for skills data")
            
        # Use static data if API is unavailable
        if not skills_data:
            skills_data = [
                {"category": "Frontend", "items": ["HTML", "CSS", "JavaScript"]},
                {"category": "Backend", "items": ["Python", "Flask", "Django"]}
            ]
        
        return render_template('skills.html', skills=skills_data, error=error_message)
    except Exception as e:
        logger.error(f"Error fetching data for skills page: {str(e)}")
        return render_template('skills.html', skills=[], error="Unable to load data. Please try again later.")

@app.route('/projects')
def projects():
    """Render the projects page"""
    projects_data = []
    error_message = None
    
    try:
        # Fetch projects data
        try:
            projects_response = requests.get(f"{BACKEND_API_URL}/projects", timeout=2)
            if projects_response.status_code == 200:
                projects_data = projects_response.json()
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for projects data")
        
        # Use static data if API is unavailable
        if not projects_data:
            projects_data = [
                {
                    "id": 1,
                    "title": "Portfolio Website",
                    "description": "My personal portfolio website",
                    "technologies": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
                    "category": "Web Development",
                    "image": "project1.jpg",
                    "github_url": "https://github.com/arpit-pal",
                    "live_url": "#"
                }
            ]
            
        # Get filter parameter if any
        filter_category = request.args.get('category', 'all')
        
        # Filter projects by category if needed
        if filter_category != 'all':
            filtered_projects = [p for p in projects_data if p.get('category') == filter_category]
        else:
            filtered_projects = projects_data
            
        # Get unique categories for the filter dropdown
        categories = sorted(set(p.get('category', '') for p in projects_data if p.get('category')))
        
        return render_template('projects.html', 
                              projects=filtered_projects,
                              categories=categories,
                              selected_category=filter_category,
                              error=error_message)
    except Exception as e:
        logger.error(f"Error fetching data for projects page: {str(e)}")
        return render_template('projects.html', 
                               projects=[],
                               categories=[],
                               selected_category='all',
                               error="Unable to load data. Please try again later.")

@app.route('/experience')
def experience():
    """Render the experience page"""
    experience_data = []
    error_message = None
    
    try:
        # Fetch experience data
        try:
            experience_response = requests.get(f"{BACKEND_API_URL}/experience", timeout=2)
            if experience_response.status_code == 200:
                experience_data = experience_response.json()
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for experience data")
        
        # Use static data if API is unavailable
        if not experience_data:
            experience_data = [
                {
                    "id": 1,
                    "company": "Example Company",
                    "title": "Software Developer",
                    "description": "Worked on various web development projects",
                    "start_date": "2020-01-01",
                    "end_date": "2023-01-01",
                    "type": "job"
                }
            ]
            
        # Get filter parameter if any
        filter_type = request.args.get('type', 'all')
        
        # Filter experience if needed
        if filter_type != 'all':
            filtered_experience = [e for e in experience_data if e.get('type', '').lower() == filter_type.lower()]
        else:
            filtered_experience = experience_data
            
        return render_template('experience.html', 
                               experience=filtered_experience,
                               filter=filter_type,
                               error=error_message)
    except Exception as e:
        logger.error(f"Error fetching data for experience page: {str(e)}")
        return render_template('experience.html', 
                               experience=[],
                               filter='all',
                               error="Unable to load data. Please try again later.")

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        # Get form data
        contact_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'subject': request.form.get('subject'),
            'message': request.form.get('message')
        }
        
        # Send data to backend
        try:
            response = requests.post(f"{BACKEND_API_URL}/contact", json=contact_data, timeout=2)
            
            if response.status_code == 200:
                return render_template('contact.html', success="Your message has been sent successfully!")
            else:
                return render_template('contact.html', error="Failed to send message. Please try again later.")
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for contact submission")
            # Store message locally or in session if backend is unavailable
            return render_template('contact.html', 
                                  success="Your message has been received. We'll get back to you soon!",
                                  note="Note: Backend service is currently unavailable, but your message has been recorded.")
    except Exception as e:
        logger.error(f"Error submitting contact form: {str(e)}")
        return render_template('contact.html', error="An error occurred. Please try again later.")

@app.route('/chatbot')
def chatbot():
    """Render the chatbot interface"""
    return render_template('chatbot.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chatbot API requests"""
    try:
        # Get user message
        user_message = request.json.get('message', '')
        
        # Forward to AI chatbot service
        try:
            response = requests.post(f"{BACKEND_API_URL}/chatbot", json={'message': user_message}, timeout=2)
            
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                return jsonify({'error': 'Failed to get response from chatbot service'}), 500
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for chatbot")
            # Provide a fallback response when backend is unavailable
            return jsonify({
                'message': "I'm sorry, I'm currently offline. Please try again later or contact me through the contact form.",
                'offline': True
            })
    except Exception as e:
        logger.error(f"Error in chatbot API: {str(e)}")
        return jsonify({'error': 'An error occurred processing your request'}), 500

# Admin routes
@app.route('/admin')
@login_required
def admin():
    """Render the admin dashboard"""
    return render_template('admin/dashboard.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    """Handle admin login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Authenticate with backend
        auth_data = {'username': username, 'password': password}
        try:
            response = requests.post(f"{BACKEND_API_URL}/auth/login", json=auth_data, timeout=2)
            
            if response.status_code == 200:
                auth_response = response.json()
                session['user_id'] = auth_response.get('userId')
                session['token'] = auth_response.get('token')
                return redirect(url_for('admin'))
            else:
                return render_template('admin/login.html', error="Invalid credentials")
        except requests.exceptions.ConnectionError:
            logger.warning("Backend API not available for authentication")
            return render_template('admin/login.html', error="Authentication service is currently unavailable. Please try again later.")
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
def logout():
    """Handle admin logout"""
    session.clear()
    return redirect(url_for('index'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true') 