from flask import Blueprint, request, jsonify
from chatbot import PortfolioChatbot
import os
from datetime import datetime

# Create a blueprint for the chatbot API routes
chatbot_api = Blueprint('chatbot_api', __name__)

# Initialize the chatbot
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
chatbot = PortfolioChatbot(data_dir)

@chatbot_api.route('/chat', methods=['POST'])
def chat():
    """Handle chatbot interactions"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({
                'success': False,
                'message': 'No message provided'
            }), 400
        
        # Get response from chatbot
        response = chatbot.get_response(user_message)
        
        # Save conversation periodically (every 10 messages)
        if len(chatbot.conversation_history) % 10 == 0:
            chatbot.save_conversation()
        
        return jsonify({
            'success': True,
            'response': response,
            'timestamp': datetime.now().strftime('%H:%M')
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

@chatbot_api.route('/reset', methods=['POST'])
def reset_conversation():
    """Reset the chatbot conversation"""
    try:
        # Save the current conversation
        if chatbot.conversation_history:
            chatbot.save_conversation()
        
        # Reset conversation history
        chatbot.conversation_history = []
        
        return jsonify({
            'success': True,
            'message': 'Conversation reset successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500 