import http.server
import socketserver
import socket

PORT = 8000  # Можно изменить порт
DIRECTORY = "."  # Папка с сайтом

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Получаем локальный IP
hostname = socket.gethostbyname(socket.gethostname())

# Запуск сервера
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен! Открывай в браузере:\n")
    print(f"➡  Локально:     http://localhost:{PORT}")
    print(f"➡  В сети:       http://{hostname}:{PORT}\n")
    print("Нажми CTRL+C, чтобы остановить сервер.")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")