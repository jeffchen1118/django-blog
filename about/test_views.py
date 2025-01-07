from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About, CollaborateRequest

class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About.objects.create(
            title="About title",
            content="About content"
        )

    def test_render_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_submit_collaborate_form(self):
        post_data = {
            'name': 'myName',
            'email': 'test@test.com',
            'message': 'Hello!'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaborate form request received, I endeavour to respond within 2 working days.",
            response.content
        )








 