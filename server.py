import socket, struct, pickle, cv2

# Define the server IP and port
SERVER_PORT = 9999  # Choose a port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
socket_address = (host_ip, SERVER_PORT)

#bind
server_socket.bind((socket_address))

# Listen for incoming connections
server_socket.listen(5)
print("[*] Listening at: ", socket_address)

# Accept a single connection and make a socket object
while True:
    client_socket, address = server_socket.accept()
    print(f"[+] {address} is connected.")
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a))+a
            client_socket.sendall(message)
            cv2.imshow("TRANSMITTING VIDEO", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()