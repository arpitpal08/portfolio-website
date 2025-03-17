# Arpit Pal - Portfolio Website

A modern, responsive portfolio website for Arpit Pal, showcasing his skills, projects, experience, and providing a way to get in touch.

## Features

- **Responsive Design**: Looks great on all devices
- **Dark Mode Support**: Automatically adapts to user preferences
- **Interactive UI**: Modern and engaging user interface
- **AI Assistant**: Chat with an AI to learn more about Arpit
- **Contact Form**: Easy way to get in touch

## Pages

- **Home**: Landing page with key highlights
- **About**: Detailed information about Arpit's background
- **Skills**: Comprehensive overview of technical skills
- **Projects**: Showcase of portfolio projects
- **Experience**: Professional experience and achievements
- **Contact**: Contact form and information
- **AI Chatbot**: Interactive AI assistant

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Flask (Python)
- **Templating**: Jinja2
- **Icons**: Font Awesome
- **Animations**: CSS animations, Typed.js
- **Charts**: Chart.js

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/arpit-portfolio.git
   cd arpit-portfolio
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
portfolio-website/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── Procfile                # For Heroku deployment
├── app.yaml                # For Google Cloud deployment
├── netlify.toml            # For Netlify deployment
├── frontend/
│   ├── static/             # Static files (CSS, JS, images)
│   │   ├── css/            # CSS files
│   │   ├── js/             # JavaScript files
│   │   ├── images/         # Images
│   │   └── files/          # Downloadable files (e.g., resume)
│   └── templates/          # HTML templates
│       ├── base.html       # Base template
│       ├── index.html      # Home page
│       ├── about.html      # About page
│       ├── skills.html     # Skills page
│       ├── projects.html   # Projects page
│       ├── experience.html # Experience page
│       ├── contact.html    # Contact page
│       ├── chatbot.html    # AI Chatbot page
│       ├── 404.html        # 404 error page
│       └── 500.html        # 500 error page
├── backend/
│   ├── data/               # Data storage
│   │   ├── messages.json   # Stored contact messages
│   │   └── projects.json   # Project data
│   └── src/                # Backend source code
│       ├── __init__.py     # Package initialization
│       ├── models.py       # Data models
│       ├── routes.py       # API routes
│       └── services.py     # Business logic services
└── ai-chatbot/
    ├── __init__.py         # Package initialization
    ├── chatbot.py          # Chatbot implementation
    ├── routes.py           # Chatbot API routes
    └── data/               # Chatbot data
        ├── knowledge_base.json  # Chatbot knowledge base
        └── conversations/   # Stored conversations
```

## Customization

To customize this portfolio for your own use:

1. Update personal information in the templates
2. Replace images in the `frontend/static/images/` directory
3. Modify the chatbot responses in `app.py`
4. Update the color scheme by changing CSS variables in `base.html`

## Deployment

### Heroku

1. Create a `Procfile` with:
   ```
   web: gunicorn app:app
   ```

2. Deploy to Heroku:
   ```
   heroku create your-app-name
   git push heroku main
   ```

### Other Platforms

The application can be deployed on any platform that supports Python/Flask applications, such as:

- PythonAnywhere
- DigitalOcean
- AWS
- Vercel

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Bootstrap for the responsive framework
- Font Awesome for the icons
- Chart.js for the interactive charts
- Typed.js for the typing animation

## Contact Information

- **Name:** Arpit Pal
- **Email:** palarpit894@gmail.com
- **Phone:** 9873765528
- **LinkedIn:** [Arpit Pal](https://www.linkedin.com/in/contactarpitpal)
- **GitHub:** [github.com/arpitpal20](https://github.com/arpitpal20)

## Deployment

The application is designed to be cloud-ready (GCP, AWS, or Azure) but also deployable on Netlify as a secondary option. 

## Deploying to Amazon Web Services (AWS)

For AWS, we'll use Elastic Beanstalk which is ideal for Flask applications:

1. **Install AWS CLI and EB CLI**:
   ```
   pip install awscli awsebcli
   ```

2. **Create configuration files**:

## Deploy to GCP

```
gcloud init
gcloud app deploy
```

## API Endpoints

The portfolio website includes several API endpoints:

### Backend API

- **GET /api/projects**: Get all projects or filter by category
- **GET /api/projects/<project_id>**: Get a specific project by ID
- **POST /api/contact**: Submit a contact form message

### Chatbot API

- **POST /api/chatbot/chat**: Send a message to the chatbot and get a response
- **POST /api/chatbot/reset**: Reset the chatbot conversation

## AI Chatbot

The portfolio includes an AI chatbot that can answer questions about Arpit's:

- Skills and expertise
- Projects and portfolio
- Work experience
- Education
- Contact information
- Specific areas like cybersecurity, AI/ML, or backend development

The chatbot uses a keyword-based approach with predefined responses stored in a knowledge base. In a production environment, this could be enhanced with:

- Natural Language Processing (NLP) libraries
- Integration with a language model API
- Machine learning for response improvement 