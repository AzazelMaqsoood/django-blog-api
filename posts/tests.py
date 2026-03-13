from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        """Проверяет, что пост создается корректно"""
        post = Post.objects.create(title="Test", content="Content")
        self.assertEqual(post.title, "Test")
        self.assertIsNotNone(post.created_at)