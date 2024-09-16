import socket

host = input("Digite o host/Ip:")
porta = int(input("Digite a porta:"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	client.connect((host, porta))
	print("\033[32mConexão estabelecida")

	while True:

			mensagem = input("Mensagem: ")
			client.send(mensagem.encode())

			dados = client.recv(2048).decode()
			print("Servidor: {}".format(dados))

			if mensagem.lower().strip() == "sair":
				print("Conexão fechada")
				break

			if dados.lower().strip().split() == "sair":
				print("\033[33mConexão fechada")
				break

	client.close()

except Exception as error:
	print("Erro ao se conectar!!!")
	print(error)