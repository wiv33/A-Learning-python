import socket

with socket.socket() as s:
    s.bind(('0.0.0.0', 12345))
    s.listen()

    print("server is started")

    conn, address = s.accept()

    with conn:
        print("connected by", address)

        while True:
            data = conn.recv(1024)

            if not data:
                break

            conn.sendall(data)
            
