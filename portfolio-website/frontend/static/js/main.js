/**
 * Arpit Pal Portfolio - Main JavaScript
 * Handles interactive features and animations
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate On Scroll) if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true
        });
    }

    // Dark Mode Toggle
    const themeToggle = document.getElementById('theme-toggle');
    
    if (themeToggle) {
        // Check for saved theme preference or use system preference
        const savedTheme = localStorage.getItem('theme');
        
        if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.body.classList.add('dark-theme');
        }
        
        // Toggle dark mode
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            
            // Save preference
            if (document.body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // Project Filters
    const projectFilters = document.querySelectorAll('.project-filter');
    const projectCards = document.querySelectorAll('.project-card');
    
    if (projectFilters.length > 0) {
        projectFilters.forEach(filter => {
            filter.addEventListener('click', function() {
                // Remove active class from all filters
                projectFilters.forEach(f => f.classList.remove('active'));
                
                // Add active class to clicked filter
                this.classList.add('active');
                
                const category = this.getAttribute('data-filter');
                
                // Filter projects
                if (category === 'all') {
                    projectCards.forEach(card => {
                        card.style.display = 'block';
                    });
                } else {
                    projectCards.forEach(card => {
                        if (card.getAttribute('data-categories').includes(category)) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                }
            });
        });
    }
    
    // Experience Filters
    const experienceFilters = document.querySelectorAll('.experience-filter');
    const experienceCards = document.querySelectorAll('.experience-card');
    
    if (experienceFilters.length > 0) {
        experienceFilters.forEach(filter => {
            filter.addEventListener('click', function() {
                // Remove active class from all filters
                experienceFilters.forEach(f => f.classList.remove('active'));
                
                // Add active class to clicked filter
                this.classList.add('active');
                
                const type = this.getAttribute('data-filter');
                
                // Filter experiences
                if (type === 'all') {
                    experienceCards.forEach(card => {
                        card.style.display = 'block';
                    });
                } else {
                    experienceCards.forEach(card => {
                        if (card.getAttribute('data-type') === type) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                }
            });
        });
    }
    
    // Contact Form Options
    const contactOptions = document.querySelectorAll('.contact-option');
    const contactForms = document.querySelectorAll('.contact-form-container');
    
    if (contactOptions.length > 0) {
        contactOptions.forEach(option => {
            option.addEventListener('click', function() {
                // Remove active class from all options
                contactOptions.forEach(o => o.classList.remove('active'));
                
                // Add active class to clicked option
                this.classList.add('active');
                
                const formType = this.getAttribute('data-form');
                
                // Show selected form
                contactForms.forEach(form => {
                    if (form.getAttribute('id') === formType) {
                        form.style.display = 'block';
                    } else {
                        form.style.display = 'none';
                    }
                });
            });
        });
    }
    
    // Contact Form Validation
    const contactForm = document.getElementById('contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let isValid = true;
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            
            // Reset error messages
            document.querySelectorAll('.error-message').forEach(el => el.remove());
            
            // Validate name
            if (!nameInput.value.trim()) {
                isValid = false;
                showError(nameInput, 'Please enter your name');
            }
            
            // Validate email
            if (!isValidEmail(emailInput.value.trim())) {
                isValid = false;
                showError(emailInput, 'Please enter a valid email address');
            }
            
            // Validate message
            if (!messageInput.value.trim()) {
                isValid = false;
                showError(messageInput, 'Please enter your message');
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    }
    
    // Chatbot functionality
    const chatbotContainer = document.querySelector('.chatbot-container');
    
    if (chatbotContainer) {
        const chatMessages = document.querySelector('.chat-messages');
        const chatInput = document.querySelector('.chat-input input');
        const chatButton = document.querySelector('.chat-input button');
        
        // Function to add a message to the chat
        function addMessage(message, isUser = false) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message');
            messageElement.classList.add(isUser ? 'message-user' : 'message-bot');
            messageElement.textContent = message;
            
            chatMessages.appendChild(messageElement);
            
            // Scroll to bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        // Add welcome message
        addMessage('Hi there! I\'m Arpit\'s AI assistant. How can I help you today?');
        
        // Handle send button click
        chatButton.addEventListener('click', sendMessage);
        
        // Handle enter key press
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        // Function to send message
        function sendMessage() {
            const message = chatInput.value.trim();
            
            if (message) {
                // Add user message to chat
                addMessage(message, true);
                
                // Clear input
                chatInput.value = '';
                
                // Show typing indicator
                const typingIndicator = document.createElement('div');
                typingIndicator.classList.add('message', 'message-bot', 'typing-indicator');
                typingIndicator.innerHTML = '<span></span><span></span><span></span>';
                chatMessages.appendChild(typingIndicator);
                
                // Scroll to bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;
                
                // Send message to backend
                fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: message })
                })
                .then(response => response.json())
                .then(data => {
                    // Remove typing indicator
                    document.querySelector('.typing-indicator').remove();
                    
                    // Add bot response
                    addMessage(data.response || 'Sorry, I couldn\'t process your request.');
                })
                .catch(error => {
                    // Remove typing indicator
                    document.querySelector('.typing-indicator').remove();
                    
                    // Add error message
                    addMessage('Sorry, there was an error processing your request. Please try again later.');
                    console.error('Error:', error);
                });
            }
        }
    }
    
    // Animated counters for stats
    const statNumbers = document.querySelectorAll('.stat-number');
    
    if (statNumbers.length > 0) {
        const options = {
            threshold: 0.5
        };
        
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const countValue = target.getAttribute('data-count');
                    
                    // Check if the value contains non-numeric characters like "+"
                    if (countValue.includes('+')) {
                        // For values like "1.5+", animate to the numeric part and then add the "+" at the end
                        const numericPart = parseFloat(countValue);
                        let count = 0;
                        const duration = 2000; // 2 seconds
                        const interval = duration / (numericPart * 10); // Multiply by 10 for smoother animation
                        
                        const counter = setInterval(function() {
                            count += 0.1;
                            target.textContent = Math.round(count * 10) / 10; // Round to 1 decimal place
                            
                            if (count >= numericPart) {
                                clearInterval(counter);
                                target.textContent = countValue; // Set the full text including "+"
                            }
                        }, interval);
                    } else {
                        // For regular integer values
                        const countTo = parseInt(countValue);
                        let count = 0;
                        const duration = 2000; // 2 seconds
                        const interval = duration / countTo;
                        
                        const counter = setInterval(function() {
                            count++;
                            target.textContent = count;
                            
                            if (count >= countTo) {
                                clearInterval(counter);
                            }
                        }, interval);
                    }
                    
                    observer.unobserve(target);
                }
            });
        }, options);
        
        statNumbers.forEach(number => {
            observer.observe(number);
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Adjust for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Typing effect for hero section
    const heroTitle = document.querySelector('.hero-title .typing-text');
    
    if (heroTitle) {
        const text = heroTitle.getAttribute('data-text');
        heroTitle.textContent = '';
        
        let i = 0;
        const typingInterval = setInterval(function() {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
            } else {
                clearInterval(typingInterval);
            }
        }, 100);
    }
});

// Helper functions
function isValidEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function showError(input, message) {
    const errorElement = document.createElement('div');
    errorElement.classList.add('error-message');
    errorElement.textContent = message;
    errorElement.style.color = 'var(--accent-tertiary)';
    errorElement.style.fontSize = '0.8rem';
    errorElement.style.marginTop = '0.25rem';
    
    input.parentNode.appendChild(errorElement);
    input.style.borderColor = 'var(--accent-tertiary)';
} 