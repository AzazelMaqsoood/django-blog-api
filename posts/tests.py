from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()


class PostModelTest(TestCase):
    def test_post_creation(self):
        """Проверяет, что пост создается корректно"""
        # 1. Создаем пользователя
        user = User.objects.create_user(username="testuser", password="testpass")

        # 2. Создаем пост с автором
        post = Post.objects.create(title="Test", content="Content", author=user)

        # 3. Проверяем
        self.assertEqual(post.title, "Test")
        self.assertIsNotNone(post.created_at)
        self.assertEqual(post.author, user)
