from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from jobs.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') # use Django Test Client
        self.assertTemplateUsed(response, 'jobs/home.html')