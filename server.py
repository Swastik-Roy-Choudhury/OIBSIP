import socket

# Server-side code for the chat application
def start_server():
    # Define the server address and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Localhost and port 12345
    server_socket.listen(1)
    
    print("Server is running and waiting for connections...")
    
    # Accept connection from the client
    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")
    
    # Continuously listen for messages from the client
    while True:
        message = conn.recv(1024).decode()
        if not message:
            print("Client disconnected.")
            break
        print(f"Client: {message}")
        
        # Send a message back to the client
        response = input("You (Server): ")
        conn.send(response.encode())
    
    # Close the connection
    conn.close()

# Run the server
start_server()