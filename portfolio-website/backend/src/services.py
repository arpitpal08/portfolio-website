import json
import os
from datetime import datetime
from .models import ContactMessage, Project

class DataService:
    """Service for handling data operations"""
    
    def __init__(self, data_dir='data'):
        """Initialize the data service"""
        self.data_dir = data_dir
        self.messages_file = os.path.join(data_dir, 'messages.json')
        self.projects_file = os.path.join(data_dir, 'projects.json')
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize files if they don't exist
        if not os.path.exists(self.messages_file):
            with open(self.messages_file, 'w') as f:
                json.dump([], f)
        
        if not os.path.exists(self.projects_file):
            with open(self.projects_file, 'w') as f:
                json.dump([], f)
    
    def save_message(self, message):
        """Save a contact message"""
        messages = self._load_messages()
        messages.append(message.to_dict())
        
        with open(self.messages_file, 'w') as f:
            json.dump(messages, f, indent=2)
        
        return True
    
    def get_messages(self):
        """Get all contact messages"""
        messages_data = self._load_messages()
        return [ContactMessage.from_dict(data) for data in messages_data]
    
    def _load_messages(self):
        """Load messages from file"""
        try:
            with open(self.messages_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_project(self, project):
        """Save a project"""
        projects = self._load_projects()
        projects.append(project.to_dict())
        
        with open(self.projects_file, 'w') as f:
            json.dump(projects, f, indent=2)
        
        return True
    
    def get_projects(self, category=None):
        """Get all projects, optionally filtered by category"""
        projects_data = self._load_projects()
        projects = [Project.from_dict(data) for data in projects_data]
        
        if category:
            projects = [p for p in projects if p.category == category]
        
        # Sort by date (newest first)
        projects.sort(key=lambda p: p.date if isinstance(p.date, datetime) else datetime.now(), reverse=True)
        
        return projects
    
    def _load_projects(self):
        """Load projects from file"""
        try:
            with open(self.projects_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []


class EmailService:
    """Service for sending emails"""
    
    def __init__(self, sender_email=None):
        """Initialize the email service"""
        self.sender_email = sender_email or 'noreply@example.com'
    
    def send_contact_notification(self, message):
        """Send a notification email when a contact form is submitted"""
        # In a real application, this would send an email
        # For now, we'll just print to the console
        print(f"New contact form submission from {message.name} ({message.email})")
        print(f"Subject: {message.subject}")
        print(f"Message: {message.message}")
        
        return True 