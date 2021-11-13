import socket

url = "hasthelargehadroncolliderdestroyedtheworldyet.com" # Test

web = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
web.connect((url, 80))
cmd = str("GET http://" + url + " HTTP/1.0\r\n\r\n").encode()
web.send(cmd)

while True:
    data = web.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

web.close()
