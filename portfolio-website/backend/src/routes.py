from flask import Blueprint, request, jsonify
from .services import DataService, EmailService
from .models import ContactMessage, Project
import os

# Create a blueprint for the API routes
api = Blueprint('api', __name__)

# Initialize services
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
data_service = DataService(data_dir)
email_service = EmailService()

@api.route('/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Create a new contact message
        message = ContactMessage(
            name=data.get('name', ''),
            email=data.get('email', ''),
            subject=data.get('subject', ''),
            message=data.get('message', '')
        )
        
        # Save the message
        data_service.save_message(message)
        
        # Send email notification
        email_service.send_contact_notification(message)
        
        return jsonify({'success': True, 'message': 'Your message has been sent successfully!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@api.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects"""
    try:
        category = request.args.get('category', None)
        projects = data_service.get_projects(category)
        return jsonify({'success': True, 'projects': projects}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@api.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """Get a specific project by ID"""
    try:
        projects = data_service.get_projects()
        project = next((p for p in projects if p.get('id') == project_id), None)
        
        if project:
            return jsonify({'success': True, 'project': project}), 200
        else:
            return jsonify({'success': False, 'message': 'Project not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500 