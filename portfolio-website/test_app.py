import unittest
import json
import os
import sys
from app import app

class PortfolioTestCase(unittest.TestCase):
    """Test case for the portfolio application"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        """Test that the home page loads"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page(self):
        """Test that the about page loads"""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
    
    def test_skills_page(self):
        """Test that the skills page loads"""
        response = self.app.get('/skills')
        self.assertEqual(response.status_code, 200)
    
    def test_projects_page(self):
        """Test that the projects page loads"""
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
    
    def test_experience_page(self):
        """Test that the experience page loads"""
        response = self.app.get('/experience')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page(self):
        """Test that the contact page loads"""
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
    
    def test_chatbot_page(self):
        """Test that the chatbot page loads"""
        response = self.app.get('/chatbot')
        self.assertEqual(response.status_code, 200)
    
    def test_api_projects(self):
        """Test the projects API endpoint"""
        response = self.app.get('/api/projects')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('projects', data)
    
    def test_chatbot_api(self):
        """Test the chatbot API endpoint"""
        response = self.app.post('/api/chatbot/chat', 
                                json={'message': 'Hello'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('response', data)

if __name__ == '__main__':
    unittest.main() 