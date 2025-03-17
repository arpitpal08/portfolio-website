from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import sys
from datetime import datetime
from backend.src.routes import api
from backend.src.services import DataService, EmailService
from backend.src.models import ContactMessage

# Add the ai-chatbot directory to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ai-chatbot'))

# Import the chatbot API blueprint
import importlib.util
spec = importlib.util.spec_from_file_location(
    "chatbot_routes", 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ai-chatbot', 'routes.py')
)
chatbot_routes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chatbot_routes)
chatbot_api = chatbot_routes.chatbot_api

app = Flask(__name__, 
            static_folder='frontend/static',
            template_folder='frontend/templates')

# Register the API blueprints
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(chatbot_api, url_prefix='/api/chatbot')

# Initialize services
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend', 'data')
data_service = DataService(data_dir)
email_service = EmailService()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Experience page
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# AI Chatbot page
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Contact form submission - Updated to use the backend service
@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_text = request.form.get('message')
        
        # Create a new contact message
        message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )
        
        # Save the message
        data_service.save_message(message)
        
        # Send email notification
        email_service.send_contact_notification(message)
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    
    return jsonify({'success': False, 'message': 'Invalid request method'})

# Legacy chatbot API endpoint - redirects to the new endpoint
@app.route('/api/chatbot', methods=['POST'])
def chatbot_api_legacy():
    """Redirect to the new chatbot API endpoint for backward compatibility"""
    return redirect(url_for('chatbot_api.chat'), code=307)  # 307 preserves the HTTP method

def get_chatbot_response(message):
    """
    Generate a response based on the user's message.
    Enhanced keyword-based approach with more comprehensive responses.
    
    Note: This function is kept for backward compatibility but is no longer used.
    The actual chatbot logic has been moved to the ai_chatbot module.
    """
    message = message.lower()
    
    if any(word in message for word in ['skill', 'expertise', 'know', 'able', 'capable', 'proficient']):
        return """
        Arpit specializes in cybersecurity, backend development, and AI/ML. His key skills include:
        <ul>
            <li>Vulnerability Assessment & Penetration Testing (VAPT)</li>
            <li>API Security and Development</li>
            <li>RAG Systems and AI Chatbots</li>
            <li>Backend Development with Java, Spring Boot, and Python</li>
            <li>Security Auditing and Incident Response</li>
            <li>Machine Learning and Data Analysis</li>
            <li>Cloud Infrastructure (AWS, Azure)</li>
        </ul>
        """
    
    elif any(word in message for word in ['project', 'work', 'portfolio', 'showcase', 'built']):
        return """
        Arpit has worked on several notable projects, including:
        <ul>
            <li>Secure File Sharing System with end-to-end encryption</li>
            <li>AI-Powered Threat Detection using machine learning</li>
            <li>Microservices Architecture Demo for scalable e-commerce</li>
            <li>Vulnerability Scanner for web applications</li>
            <li>Sentiment Analysis API with visualization dashboard</li>
            <li>This Portfolio Website with AI chatbot integration</li>
        </ul>
        You can view details of all projects in the <a href="/projects">Projects</a> section.
        """
    
    elif any(word in message for word in ['experience', 'job', 'career', 'work', 'professional']):
        return """
        Arpit's professional experience includes:
        <ul>
            <li><strong>Business Analytics and AI Intelligence Intern</strong> at Predusk Technology (Current)
                <ul>
                    <li>Developing AI-powered analytics solutions</li>
                    <li>Implementing RAG systems for knowledge retrieval</li>
                    <li>Improving query response accuracy by 40%</li>
                </ul>
            </li>
            <li><strong>Security Management Intern</strong> at DitanBizInc (2023)
                <ul>
                    <li>Conducted security audits and vulnerability assessments</li>
                    <li>Implemented security best practices</li>
                    <li>Reduced security incidents by 45%</li>
                </ul>
            </li>
        </ul>
        For more details, please visit the <a href="/experience">Experience</a> page.
        """
    
    elif any(word in message for word in ['education', 'study', 'degree', 'university', 'college']):
        return """
        Arpit's educational background:
        <ul>
            <li><strong>B.Tech in Computer Science</strong> with specialization in Cybersecurity</li>
            <li>Relevant coursework: Network Security, Cryptography, Machine Learning, Data Structures, Algorithms</li>
            <li>Additional certifications in Cyber Security, Digital Forensics, and VAPT</li>
        </ul>
        """
    
    elif any(word in message for word in ['contact', 'email', 'reach', 'touch', 'connect']):
        return """
        You can contact Arpit through:
        <ul>
            <li>Email: palarpit894@gmail.com</li>
            <li>LinkedIn: linkedin.com/in/arpit-pal</li>
            <li>GitHub: github.com/arpit-pal</li>
            <li>Twitter: @arpit_pal_tech</li>
        </ul>
        Or use the contact form on the <a href="/contact">Contact</a> page.
        """
    
    elif any(word in message for word in ['hello', 'hi', 'hey', 'greetings', 'howdy']):
        return "Hello! I'm Arpit's AI assistant. How can I help you learn more about Arpit's skills, projects, or experience today?"
    
    elif any(word in message for word in ['thank', 'thanks', 'appreciate', 'grateful']):
        return "You're welcome! I'm glad I could help. Is there anything else you'd like to know about Arpit?"
    
    elif any(word in message for word in ['cybersecurity', 'security', 'hacking', 'penetration', 'vapt']):
        return """
        Arpit specializes in cybersecurity with expertise in:
        <ul>
            <li>Vulnerability Assessment & Penetration Testing (VAPT)</li>
            <li>Security auditing and compliance</li>
            <li>Secure coding practices</li>
            <li>API security testing</li>
            <li>Incident response and threat modeling</li>
        </ul>
        His projects in this domain include a Secure File Sharing System and a Vulnerability Scanner for web applications.
        """
    
    elif any(word in message for word in ['ai', 'ml', 'machine learning', 'artificial intelligence', 'data']):
        return """
        In the AI & ML domain, Arpit has worked on:
        <ul>
            <li>AI-Powered Threat Detection systems</li>
            <li>Sentiment Analysis API with NLP</li>
            <li>RAG (Retrieval Augmented Generation) systems</li>
            <li>Chatbot development (like me!)</li>
            <li>Data analysis and visualization</li>
        </ul>
        He uses technologies like TensorFlow, PyTorch, spaCy, and NLTK for these projects.
        """
    
    elif any(word in message for word in ['backend', 'api', 'server', 'database', 'microservices']):
        return """
        Arpit's backend development skills include:
        <ul>
            <li>API development with Flask, Django, and Spring Boot</li>
            <li>Microservices architecture design and implementation</li>
            <li>Database design and optimization (SQL and NoSQL)</li>
            <li>RESTful and GraphQL API design</li>
            <li>Containerization with Docker and orchestration with Kubernetes</li>
        </ul>
        His Microservices Architecture Demo project showcases these skills in action.
        """
    
    else:
        return """
        I'm not sure I understand. Would you like to know about Arpit's:
        <ul>
            <li>Skills and expertise</li>
            <li>Projects</li>
            <li>Work experience</li>
            <li>Education</li>
            <li>Contact information</li>
        </ul>
        Or ask me about specific areas like cybersecurity, AI/ML, or backend development!
        """

# Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Context processor to make current year available in all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs('frontend/static/images', exist_ok=True)
    os.makedirs('frontend/static/css', exist_ok=True)
    os.makedirs('frontend/static/js', exist_ok=True)
    os.makedirs('frontend/static/files', exist_ok=True)
    os.makedirs('backend/data', exist_ok=True)
    os.makedirs('ai-chatbot/data', exist_ok=True)
    
    # Run the application
    app.run(debug=True) 