import socket
import os
import random
import hashlib

# using sha256 hash_function
def get_checksum(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        res = hashlib.sha256(bytes).hexdigest()
    return res

def main():
    # Create serverdata folder
    try:
        os.mkdir(os.path.join("./","serverdata"))
    except:
        pass

    # Write random data into serverdata/data.txt file
    f = open("./serverdata/data.txt", "w")
    for i in range(20):
        randomlist = random.randint(1,100)
        f.write(str(randomlist) + '\n')
    f.close()
    
    host = socket.gethostname()
    try:
        port = os.environ["PORT"]
    except:
        port = 8081
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    connection = server_socket.accept()[0]

    # Read from serverdata/data.txt file and send it to the client
    file_to_read = open("./serverdata/data.txt", "rb")
    data = file_to_read.read(1024)
    while data:
        connection.send(data)
        data = file_to_read.read(1024)
    file_to_read.close()

    # Calculate checkSum and send it to the client
    checkSum = get_checksum("./serverdata/data.txt")
    connection.send(checkSum.encode())
    
    # Close the connection
    connection.close()

if __name__ == '__main__':
    main()