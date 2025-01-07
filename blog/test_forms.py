from django.test import TestCase
from .forms import CommentForm
# Create your tests here.

class TestCommentForm(TestCase):
    
    def test_form_is_valid(self):
        form = CommentForm(data={'body': 'This is a test comment'})
        self.assertTrue(form.is_valid(), msg='Form is not valid')
    
    def test_from_is_invalid(self):
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid(), msg='Form is valid')
       