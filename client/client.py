import os
import socket
import hashlib

# using sha256 hash_function
def get_checksum(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        res = hashlib.sha256(bytes).hexdigest()
    return res

def main():
    # Create clientdata folder
    try:
        os.mkdir(os.path.join("./","clientdata"))
    except:
        pass

    host = "server"
    try:
        port = os.environ["PORT"]
    except:
        port = 8081
    connection = socket.socket()
    connection.connect((host, port))

    # Get data from server and Write into clientdata/data.txt file
    file_to_write = open('./clientdata/data.txt', 'wb')
    data = connection.recv(1024)
    file_to_write.write(data)
    file_to_write.close()

    # Get CheckSum from server
    data = connection.recv(1024).decode()
    checkSum_from_server = data

    # Calculate checkSum to check with the received checksum from server
    calculated_checkSum = get_checksum("./clientdata/data.txt")

    if(compare_checksum(checkSum_from_server,calculated_checkSum)):
        print("CheckSum verified.")
    else:
        print("CheckSum not verified.")
    
    # Close the connection
    connection.close()

def compare_checksum(c1,c2):
    if(c1==c2):
        return True
    else:
        return False

if __name__ == '__main__':
    main()