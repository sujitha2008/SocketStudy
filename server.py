import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind(("127.0.0.1", 8080))


server_socket.listen(1)
print("Server is listening on port 8080...")


client_socket, client_address = server_socket.accept()
print("Connected with:", client_address)


data = client_socket.recv(1024).decode()
print("Client says:", data)


client_socket.send("Hello from Server!".encode())

client_socket.close()
server_socket.close()