import socket
import time

def tcp_client():
    host = "127.0.0.1"  # 目标地址
    port = 8484         # 目标端口

    # 创建 TCP 套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # 连接到服务器
            client_socket.connect((host, port))
            print(f"Connected to {host}:{port}")

            # 等待 30 秒
            print("Waiting 30 seconds...")
            time.sleep(30)

            # 发送第一个消息
            message1 = "hello1"
            client_socket.sendall(message1.encode())
            print(f"Sent: {message1}")

            # 等待 40 秒
            print("Waiting 40 seconds...")
            time.sleep(40)

            # 发送第二个消息
            message2 = "hello2"
            client_socket.sendall(message2.encode())
            print(f"Sent: {message2}")

            # 等待 5 秒
            print("Waiting 5 seconds...")
            time.sleep(5)

            # 断开连接
            print("Closing connection...")
        except ConnectionRefusedError:
            print(f"Failed to connect to {host}:{port}. Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    tcp_client()