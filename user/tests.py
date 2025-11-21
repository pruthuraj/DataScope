
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock

class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_no_credentials(self):
        """
        Tests if a user can access the home page without credentials.
        Spoiler: they can't. It's like trying to get into a secret club 
        without the password. The bouncer (our code) will just point you to the login page.
        """
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('login'))

    @patch('user.views.db')
    def test_home_successful_login(self, mock_db):
        """
        Tests if a user can login with the correct credentials.
        This is the 'open sesame' of our app. If this test fails,
        our users are locked out, and we're in trouble.
        """
        mock_collection = MagicMock()
        mock_collection.find_one.return_value = {'email': 'test@example.com'}
        mock_db.__getitem__.return_value = mock_collection

        response = self.client.get(reverse('home'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/index.html')

    def test_mine_view(self):
        """
        Tests the mine view. This is where the magic happens.
        Or, at least, where we render a page called 'mine.html'.
        Close enough.
        """
        response = self.client.get(reverse('mine'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/mine.html')

    @patch('user.views.mineUserProduct')
    def test_mindata_valid_url(self, mock_mineUserProduct):
        """
        Tests if we can mine data from a valid Amazon URL.
        It's like being a digital gold miner, but with less dirt
        and more data.
        """
        mock_mineUserProduct.return_value = MagicMock()
        response = self.client.post(reverse('mindata'), {'product_id': 'https://www.amazon.in/dp/B07X1Y2K4D'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/minedata.html')

    def test_compare_view(self):
        """
        Tests the compare view. This is where we put two products
        in a digital boxing ring and see which one comes out on top.
        Ding ding!
        """
        response = self.client.get(reverse('compare'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/compare.html')

    @patch('user.views.properCompare')
    def test_for_users_compare_view(self, mock_properCompare):
        """
        Tests the comparison results view. After the digital fisticuffs,
        this is where we announce the winner. Or, you know, just show
        a table of data.
        """
        mock_properCompare.return_value = MagicMock()
        response = self.client.get(reverse('forUsersCompare'), {'product': 'testproduct'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/compareProduct.html')

    @patch('user.views.db')
    @patch('user.views.trackProduct')
    def test_track_view_post(self, mock_trackProduct, mock_db):
        """
        Tests adding a product to the tracking list. It's like being a
        digital stalker, but for products. And it's totally legal.
        """
        mock_trackProduct.return_value = {'name': 'Test Product', 'price': '100', 'imgUrl': 'http://example.com/img.png'}
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        response = self.client.post(reverse('track'), {'purl': 'https://www.amazon.in/dp/B07X1Y2K4D'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/track.html')

    def test_request_view(self):
        """
        Tests the request view. This is where users can ask for new features.
        It's like a suggestion box, but with more code and less paper.
        """
        response = self.client.get(reverse('request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forUsers/request.html')
