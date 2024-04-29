import socket

while True:
    def receive_and_log_info(log_file_path, server_ip, server_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((server_ip, server_port))
            s.listen()
            print("Server listening...")
            conn, addr = s.accept()
            with conn:
                print("Connected by", addr)
                data = conn.recv(1024).decode()
                print("Received:", data)
                with open(log_file_path, "a") as log_file:
                    log_file.write(data + "\n")
                    print("Data logged to", log_file_path)

    if __name__ == "__main__":
        log_file_path = "logs.txt"  # ログファイルのパス
        server_ip = "0.0.0.0"  # サーバーのIPアドレス
        server_port = 25565  # サーバーのポート番号

        receive_and_log_info(log_file_path, server_ip, server_port)
