from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8080))
s.listen(5)
print(f"Aguardando conexao na porta 8080 R...")
while True:
    obj, user = s.accept()
    print(user)

#abre a porta 8080 no pc atual 
