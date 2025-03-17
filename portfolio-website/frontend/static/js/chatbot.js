/**
 * Chatbot functionality for Arpit Pal's portfolio website
 * Handles user interactions with the AI chatbot
 */

document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const chatMessages = document.getElementById('chat-messages');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const resetButton = document.getElementById('reset-button');
    const chatLoader = document.getElementById('chat-loader');
    
    // Initial greeting
    setTimeout(() => {
        addBotMessage("Hello! I'm Arpit's AI assistant. How can I help you learn more about Arpit's skills, projects, or experience today?");
    }, 500);
    
    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    if (resetButton) {
        resetButton.addEventListener('click', resetChat);
    }
    
    /**
     * Send a message to the chatbot API
     */
    function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addUserMessage(message);
        
        // Clear input
        messageInput.value = '';
        
        // Show loading indicator
        showLoader();
        
        // Send message to API
        fetch('/api/chatbot/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading indicator
            hideLoader();
            
            if (data.success) {
                // Add bot response to chat
                addBotMessage(data.response, data.timestamp);
            } else {
                // Show error message
                addBotMessage("I'm sorry, I encountered an error. Please try again later.", new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}));
            }
        })
        .catch(error => {
            // Hide loading indicator
            hideLoader();
            
            // Show error message
            console.error('Error:', error);
            addBotMessage("I'm sorry, I couldn't connect to the server. Please check your connection and try again.", new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}));
        });
    }
    
    /**
     * Reset the chat conversation
     */
    function resetChat() {
        // Confirm reset
        if (!confirm('Are you sure you want to reset the conversation?')) {
            return;
        }
        
        // Clear chat messages
        chatMessages.innerHTML = '';
        
        // Show loading indicator
        showLoader();
        
        // Send reset request to API
        fetch('/api/chatbot/reset', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading indicator
            hideLoader();
            
            // Add initial greeting
            addBotMessage("Hello! I'm Arpit's AI assistant. How can I help you learn more about Arpit's skills, projects, or experience today?");
        })
        .catch(error => {
            // Hide loading indicator
            hideLoader();
            
            // Show error message
            console.error('Error:', error);
            addBotMessage("I'm sorry, I couldn't connect to the server. Please check your connection and try again.", new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}));
        });
    }
    
    /**
     * Add a user message to the chat
     * @param {string} message - The message text
     */
    function addUserMessage(message) {
        const time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        const messageElement = document.createElement('div');
        messageElement.className = 'chat-message user-message';
        messageElement.innerHTML = `
            <div class="message-content">
                <p>${escapeHtml(message)}</p>
                <span class="message-time">${time}</span>
            </div>
            <div class="avatar">
                <i class="fas fa-user"></i>
            </div>
        `;
        chatMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    /**
     * Add a bot message to the chat
     * @param {string} message - The message text
     * @param {string} time - The message timestamp
     */
    function addBotMessage(message, time = null) {
        if (!time) {
            time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        }
        
        const messageElement = document.createElement('div');
        messageElement.className = 'chat-message bot-message';
        messageElement.innerHTML = `
            <div class="avatar">
                <i class="fas fa-robot"></i>
            </div>
            <div class="message-content">
                <div>${message}</div>
                <span class="message-time">${time}</span>
            </div>
        `;
        chatMessages.appendChild(messageElement);
        scrollToBottom();
        
        // Add click event listeners to any links in the bot message
        const links = messageElement.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                // If it's an internal link, handle it
                if (link.getAttribute('href').startsWith('/')) {
                    e.preventDefault();
                    window.location.href = link.getAttribute('href');
                }
            });
        });
    }
    
    /**
     * Show the loading indicator
     */
    function showLoader() {
        if (chatLoader) {
            chatLoader.style.display = 'flex';
        }
    }
    
    /**
     * Hide the loading indicator
     */
    function hideLoader() {
        if (chatLoader) {
            chatLoader.style.display = 'none';
        }
    }
    
    /**
     * Scroll the chat to the bottom
     */
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    /**
     * Escape HTML special characters to prevent XSS
     * @param {string} unsafe - The unsafe string
     * @returns {string} - The escaped string
     */
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
}); 