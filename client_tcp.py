import socket
import sys

help_msg = "Usage: python3 client_tcp.py [SERVER] [PORT]"

# socket creation passing the arguments (family, type)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# exception handling
try:
    n = len(sys.argv)
    if n != 3:
        raise ValueError("This programs takes exactly two arguments")
    arguments = []
    for i in range(1, n):
        arguments.append(sys.argv[i])
    # connect the socket to a host
    client.connect((arguments[0], int(arguments[1])))
    while True:
        # send data to the host (encoding the string to bytes)
        msg = input("Message: ")+"\n"
        if msg == "quit\n" or msg == "exit\n":
            client.send(msg.encode())
            break
        client.send(msg.encode())
        # save the response into a variable (decoding bytes to string)
        response = client.recv(1020).decode()
        if response == "quit\n" or response == "exit\n":
            print("Connection closed by remote server")
            break
        print(response)
except Exception as error:
    print("Error:", error)
