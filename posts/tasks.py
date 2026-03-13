from celery import shared_task
import time

@shared_task
def debug_task():
    print("🔄 Задача запущена в фоне!")
    time.sleep(2)  # Имитация долгой работы
    print("✅ Задача выполнена!")
    return "Success"