from datetime import datetime

class ContactMessage:
    """Model for storing contact form messages"""
    
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.timestamp = datetime.now()
        self.is_read = False
    
    def to_dict(self):
        """Convert the message to a dictionary"""
        return {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'timestamp': self.timestamp.isoformat(),
            'is_read': self.is_read
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a message from a dictionary"""
        message = cls(
            name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('message')
        )
        message.timestamp = datetime.fromisoformat(data.get('timestamp'))
        message.is_read = data.get('is_read', False)
        return message


class Project:
    """Model for storing project information"""
    
    def __init__(self, title, description, image_url, github_url=None, live_url=None, 
                 technologies=None, category=None, date=None):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.github_url = github_url
        self.live_url = live_url
        self.technologies = technologies or []
        self.category = category
        self.date = date or datetime.now()
    
    def to_dict(self):
        """Convert the project to a dictionary"""
        return {
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'github_url': self.github_url,
            'live_url': self.live_url,
            'technologies': self.technologies,
            'category': self.category,
            'date': self.date.isoformat() if isinstance(self.date, datetime) else self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a project from a dictionary"""
        project = cls(
            title=data.get('title'),
            description=data.get('description'),
            image_url=data.get('image_url'),
            github_url=data.get('github_url'),
            live_url=data.get('live_url'),
            technologies=data.get('technologies', []),
            category=data.get('category')
        )
        
        date = data.get('date')
        if date:
            try:
                project.date = datetime.fromisoformat(date)
            except (ValueError, TypeError):
                project.date = date
                
        return project 