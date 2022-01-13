import socket
import sys

# help message
help_msg = 'Usage: python3 server_tcp.py [PORT]'

# socket creation passing the arguments (family, type)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# exception handling
try:
    # receiving and working with command line arguments
    n = len(sys.argv)
    if n == 1 or sys.argv[1] == 'help':
        print(help_msg)
        exit()
    if n != 2:
        raise ValueError('This programs takes exactly one argument\n' + help_msg)
    # set the IP and port to listen
    port = int(sys.argv[1])
    server.bind(('0.0.0.0', port))
    # set how many simultaneous connections the server will accept
    server.listen(3)
    print('Listening on {0}...'.format(port))
    # accept the connections
    client_socket, client_address = server.accept()
    print('Connection from: ' + client_address[0])
    while True:
        data = client_socket.recv(1024).decode()
        # verify if it's a escape message
        if data == 'quit\n' or data == 'exit\n':
            print('Connection closed by remote client')
            break
        print('Client says: ' + data.strip('\n'))
        msg = input('Message: ')+'\n'
        print()
        # verify if it's a escape message
        if msg == 'quit\n' or msg == 'exit\n':
            client_socket.send(msg.encode())
            break
        client_socket.send(msg.encode())
    server.close()
except Exception as error:
    print(help_msg)
    print('Error:', error)
    server.close()
