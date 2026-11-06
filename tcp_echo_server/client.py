import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("================================")
print("TCP Echo Client")
print("================================")

try:
    client_socket.connect((HOST, PORT))

    print(f"Connected to server {HOST}:{PORT}")
    print("Type a message and press Enter.")
    print("Type 'exit' to quit.")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            break

        client_socket.send(message.encode("utf-8"))

        data = client_socket.recv(1024)

        response = data.decode("utf-8")

        print(f"Server: {response}")

finally:
    client_socket.close()
    print("Disconnected from server.")
