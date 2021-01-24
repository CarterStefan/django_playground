from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        reponse = self.client.get('/')
        self.assertEqual(reponse.status_code, 200)

    def test_about_page_status_code(self):
        reponse = self.client.get('/about/')
        self.assertEqual(reponse.status_code, 200)
