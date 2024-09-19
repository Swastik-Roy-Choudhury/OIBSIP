import socket

# Client-side code for the chat application
def start_client():
    # Define the server address and port to connect to
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connect to localhost on port 12345
    
    print("Connected to the server. You can start chatting!")
    
    # Continuously send and receive messages
    while True:
        message = input("You (Client): ")
        client_socket.send(message.encode())
        
        # Receive a response from the server
        response = client_socket.recv(1024).decode()
        if not response:
            print("Server disconnected.")
            break
        print(f"Server: {response}")
    
    # Close the connection
    client_socket.close()

# Run the client
start_client()