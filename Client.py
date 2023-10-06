import socket
Client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Client.connect(('localhost',10))
for _ in range(3): 
    operation= input("Enter Operation(Random/Add/Subtract):")
    num1= input("Enter first number:")
    num2= input("Enter second number:")
    request = f"{operation};{num1};{num2}"
    Client.send(request.encode())
    response = Client.recv(1024).decode()
    print(f"Server response:{response}")



Client.close
