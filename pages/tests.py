
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock

class PagesViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        """
        Tests the index view. If this fails, the entire internet
        might as well be down. Just kidding. Or am I?
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_signup_view(self):
        """
        Tests the signup view. This is the gateway for new users.
        If this is broken, we're basically a closed club.
        """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SignUp.html')

    def test_login_view(self):
        """
        Tests the login view. You shall not pass! Unless you have
        the right credentials, of course.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    @patch('pages.views.db')
    def test_create_user_view(self, mock_db):
        """
        Tests the createUser view. It's like a digital assembly line
        for users. Except less greasy and more buggy.
        """
        mock_collection = MagicMock()
        mock_collection.find_one.return_value = None
        mock_collection.insert_one.return_value = MagicMock(inserted_id='some_id')
        mock_db.__getitem__.return_value = mock_collection
        response = self.client.post(reverse('createUser'), {'usid': 'testuser'})
        self.assertEqual(response.status_code, 200)

    @patch('pages.views.db')
    def test_forgot_password_view(self, mock_db):
        """
        Tests the forgotPassword view. For when your brain decides
        to go on a vacation and forgets your password.
        """
        mock_collection = MagicMock()
        mock_collection.find_one.return_value = {'email': 'test@example.com'}
        mock_db.__getitem__.return_value = mock_collection
        response = self.client.get(reverse('forgotPassword'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'passwordOTP.html')

    @patch('pages.views.db')
    def test_password_otp_view(self, mock_db):
        """
        Tests the passwordOTP view. It's like a secret handshake
        to prove you are who you say you are. But with numbers.
        """
        with patch('pages.views.otp', 1234):
            response = self.client.get(reverse('passwordOTP'), {'ot1': '1', 'ot2': '2', 'ot3': '3', 'ot4': '4'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resetPassword.html')

    def test_about_view(self):
        """
        Tests the about view. This is where we tell our life story.
        It's a real page-turner.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_view(self):
        """
        Tests the contact view. Have a question? A comment? A complaint?
        This is the place to shout into the digital void.
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
