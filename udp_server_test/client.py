import socket

HOST = "127.0.0.1"
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("================================")
print("UDP Client")
print("================================")

try:
    print(f"UDP Client is ready.")
    print(f"Sending messages to {HOST}:{PORT}")
    print("Type a message and press Enter.")
    print("Type 'exit' to quit.")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            break

        client_socket.sendto(
            message.encode("utf-8"),
            (HOST, PORT)
        )

        data, server_address = client_socket.recvfrom(1024)

        response = data.decode("utf-8")

        print(f"Server: {response}")

finally:
    client_socket.close()
    print("Client stopped.")