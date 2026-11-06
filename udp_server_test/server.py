import socket

HOST = "127.0.0.1"
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))

print("================================")
print("UDP Server")
print("================================")
print(f"Server is running on {HOST}:{PORT}")
print("Waiting for messages...")
print("Press Ctrl+C to stop the server.")

try:
    while True:
        data, client_address = server_socket.recvfrom(1024)

        message = data.decode("utf-8")

        print(f"\nReceived from {client_address}: {message}")

        response = f"UDP Echo: {message}"

        server_socket.sendto(
            response.encode("utf-8"),
            client_address
        )

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server_socket.close()