import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5050))

while True:
	client.send(input("").encode())
	dados = client.recv(2048).decode()
	print(dados)
