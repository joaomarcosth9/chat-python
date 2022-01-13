import socket

# socket creation passing the arguments (family, type)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # set the IP and port to listen
    port = 4433
    server.bind(("0.0.0.0", port))
    # set how many simultaneous connections the server will accept
    server.listen(3)
    print("Listening on {0}...".format(port))
    # accept the connections
    client_socket, client_address = server.accept()
    print("Connection from: " + client_address[0])
    while True:
        data = client_socket.recv(1024).decode()
        if data == "quit\n" or data == "exit\n":
            print("Connection closed by remote client")
            break
        print(data)
        msg = input("Message: ")+"\n"
        if msg == "quit\n" or msg == "exit\n":
            client_socket.send(msg.encode())
            break
        client_socket.send(msg.encode())
    server.close()
except Exception as error:
    print("Error:", error)
    server.close()
