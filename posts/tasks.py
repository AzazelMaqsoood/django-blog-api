from celery import shared_task
import time

@shared_task
def debug_task():
    print("🔄 Задача запущена в фоне!")
    time.sleep(2)  # Имитация долгой работы
    print("✅ Задача выполнена!")
    return "Success"

@shared_task
def send_post_notification(post_id, author_username):
    """
    Имитирует отправку уведомления о новом посте.
    """
    print(f"📧 Отправка уведомления для поста #{post_id}...")
    print(f"👤 Получатель: {author_username}")
    # Здесь мог бы быть код отправки email:
    # send_mail(subject, message, from_email, [recipient_list])
    time.sleep(1)  # Имитация работы почтового сервера
    print(f"✅ Уведомление для поста #{post_id} отправлено!")
    return f"Notification sent for post {post_id}"    