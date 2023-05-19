import socket
'''A simple server that can accept an http connection.'''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8000))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.listen(10)

try:
    while True:
        client_socket, address = server.accept()
        recieved_data = client_socket.recv(1024).decode('utf-8')
        print("Received data on a socket: ", recieved_data)
        path = recieved_data.split(" ")[1]

        response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \
                f"Hello!<br />Path: {path}"
                
        client_socket.send(response.encode("utf-8"))
        client_socket.close()
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_RDWR)
    server.close()