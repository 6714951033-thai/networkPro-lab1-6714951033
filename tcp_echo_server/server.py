import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("================================")
print("TCP Echo Server")
print("================================")
print(f"Server is running on {HOST}:{PORT}")
print("Waiting for client...")
print("Press Ctrl+C to stop the server.")

try:
    while True:
        client_socket, client_address = server_socket.accept()

        print(f"\nClient connected: {client_address}")

        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode("utf-8")

            print(f"Received: {message}")

            response = f"Echo: {message}"

            client_socket.send(response.encode("utf-8"))

        client_socket.close()
        print("Client disconnected.")

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server_socket.close()