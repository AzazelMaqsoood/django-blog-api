from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from .tasks import send_post_notification


@receiver(post_save, sender=Post)
def trigger_notification(sender, instance, created, **kwargs):
    """
    Запускает фоновую задачу при создании нового поста.
    """
    if created:  # Важно: реагируем только на создание, не на обновление
        print(f"🔔 Сигнал получен: создан пост #{instance.id}")
        # Отправляем задачу в очередь (не ждем выполнения!)
        send_post_notification.delay(instance.id, instance.author.username)
