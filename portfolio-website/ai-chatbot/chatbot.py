import json
import os
import re
from datetime import datetime

class PortfolioChatbot:
    """
    A simple AI chatbot for the portfolio website.
    This implementation uses keyword matching and predefined responses.
    In a production environment, this could be enhanced with:
    - Natural Language Processing (NLP) libraries
    - Integration with a language model API
    - Machine learning for response improvement
    """
    
    def __init__(self, data_dir=None):
        """Initialize the chatbot with knowledge base"""
        self.data_dir = data_dir or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        self.knowledge_base = self._load_knowledge_base()
        self.conversation_history = []
        
    def _load_knowledge_base(self):
        """Load the knowledge base from JSON file"""
        kb_path = os.path.join(self.data_dir, 'knowledge_base.json')
        
        # Create default knowledge base if it doesn't exist
        if not os.path.exists(kb_path):
            os.makedirs(os.path.dirname(kb_path), exist_ok=True)
            default_kb = {
                "skills": {
                    "keywords": ["skill", "expertise", "know", "able", "capable", "proficient"],
                    "response": """
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
                },
                "projects": {
                    "keywords": ["project", "work", "portfolio", "showcase", "built", "create"],
                    "response": """
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
                },
                "experience": {
                    "keywords": ["experience", "job", "career", "work", "professional", "employment"],
                    "response": """
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
                },
                "education": {
                    "keywords": ["education", "study", "degree", "university", "college", "academic"],
                    "response": """
                    Arpit's educational background:
                    <ul>
                        <li><strong>B.Tech in Computer Science</strong> with specialization in Cybersecurity</li>
                        <li>Relevant coursework: Network Security, Cryptography, Machine Learning, Data Structures, Algorithms</li>
                        <li>Additional certifications in Cyber Security, Digital Forensics, and VAPT</li>
                    </ul>
                    """
                },
                "contact": {
                    "keywords": ["contact", "email", "reach", "touch", "connect", "message"],
                    "response": """
                    You can contact Arpit through:
                    <ul>
                        <li>Email: palarpit894@gmail.com</li>
                        <li>LinkedIn: linkedin.com/in/arpit-pal</li>
                        <li>GitHub: github.com/arpit-pal</li>
                        <li>Twitter: @arpit_pal_tech</li>
                    </ul>
                    Or use the contact form on the <a href="/contact">Contact</a> page.
                    """
                },
                "greeting": {
                    "keywords": ["hello", "hi", "hey", "greetings", "howdy", "morning", "afternoon", "evening"],
                    "response": "Hello! I'm Arpit's AI assistant. How can I help you learn more about Arpit's skills, projects, or experience today?"
                },
                "thanks": {
                    "keywords": ["thank", "thanks", "appreciate", "grateful", "gratitude"],
                    "response": "You're welcome! I'm glad I could help. Is there anything else you'd like to know about Arpit?"
                },
                "cybersecurity": {
                    "keywords": ["cybersecurity", "security", "hacking", "penetration", "vapt", "vulnerability"],
                    "response": """
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
                },
                "ai_ml": {
                    "keywords": ["ai", "ml", "machine learning", "artificial intelligence", "data", "analytics"],
                    "response": """
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
                },
                "backend": {
                    "keywords": ["backend", "api", "server", "database", "microservices", "web development"],
                    "response": """
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
                },
                "fallback": {
                    "response": """
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
                }
            }
            
            with open(kb_path, 'w') as f:
                json.dump(default_kb, f, indent=2)
            
            return default_kb
        
        try:
            with open(kb_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading knowledge base: {e}")
            return {}
    
    def get_response(self, user_message):
        """Generate a response based on the user's message"""
        if not user_message:
            return self.knowledge_base.get("fallback", {}).get("response", "I'm not sure how to respond to that.")
        
        # Add to conversation history
        self.conversation_history.append({
            "user": user_message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Process the message
        user_message = user_message.lower()
        
        # Check each topic in the knowledge base
        for topic, data in self.knowledge_base.items():
            if topic == "fallback":
                continue
                
            keywords = data.get("keywords", [])
            if any(keyword in user_message for keyword in keywords):
                response = data.get("response", "")
                
                # Add to conversation history
                self.conversation_history.append({
                    "bot": response,
                    "timestamp": datetime.now().isoformat()
                })
                
                return response
        
        # If no match found, use fallback response
        fallback_response = self.knowledge_base.get("fallback", {}).get("response", "I'm not sure how to respond to that.")
        
        # Add to conversation history
        self.conversation_history.append({
            "bot": fallback_response,
            "timestamp": datetime.now().isoformat()
        })
        
        return fallback_response
    
    def save_conversation(self):
        """Save the conversation history to a file"""
        if not self.conversation_history:
            return
            
        # Create conversations directory if it doesn't exist
        conversations_dir = os.path.join(self.data_dir, 'conversations')
        os.makedirs(conversations_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.json"
        filepath = os.path.join(conversations_dir, filename)
        
        # Save conversation to file
        with open(filepath, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
            
        return filepath

# For testing
if __name__ == "__main__":
    chatbot = PortfolioChatbot()
    
    print("Portfolio Chatbot Initialized. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Thanks for chatting.")
            chatbot.save_conversation()
            break
            
        response = chatbot.get_response(user_input)
        
        # Clean HTML tags for console output
        clean_response = re.sub(r'<.*?>', '', response)
        print(f"Chatbot: {clean_response}") 