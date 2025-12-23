import webview
from app import app
import threading
import time

def start_server():
    app.run(port=5000)

if __name__ == '__main__':
    # Flask sunucusunu ayrı bir thread'de çalıştır
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    
    # Sunucunun başlaması için kısa bir süre bekle
    time.sleep(1)

    # Masaüstü penceresini oluştur
    webview.create_window('Study Coach Genie', 'http://127.0.0.1:5000', width=1000, height=800)
    webview.start()
