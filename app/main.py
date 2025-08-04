from threading import Thread
import socket  # noqa: F401


def root():
    return b"HTTP/1.1 200 OK\r\n\r\n"

def echo(endpoint):
    res = endpoint.replace("/echo/", "", 1)
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(res)}\r\n\r\n{res}".encode("utf-8")

def user_agent(header):
    res = header.get("User-Agent")
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(res)}\r\n\r\n{res}".encode("utf-8")

def read_incoming_request(conn, buffer=1024):
    msg = b''
    next_expected = True
    while next_expected and len(msg) % buffer == 0:
        r = conn.recv(buffer)
        next_expected = len(r) == buffer
        msg += r
    return msg

def parse_request(request: bytes):
    return request.decode()

def split_request(request: str):
    header, body = request.split('\r\n\r\n')
    header_split = header.split('\r\n', 1)
    if len(header_split) == 2:
        request_line, header = header_split
    else:
        request_line, header = header_split[0], ''
    return request_line, header, body

def extract_request_line(request_line):
    verb, endpoint, http_version = request_line.split()
    return verb, endpoint, http_version

def extract_header(header_request):
    header = {}
    if not header_request:
        return header
    header_split = header_request.split('\r\n')
    for h in header_split:
        key, value = h.split(':', 1)
        header[key] = value.lstrip()
    return header

def process_connection(conn):
    request = read_incoming_request(conn)
    request = parse_request(request)
    request_line, header, body = split_request(request)
    verb, endpoint, _ = extract_request_line(request_line)
    header = extract_header(header)

    if endpoint == '/':
        response = root()
    elif endpoint.startswith('/echo/'):
        response = echo(endpoint)
    elif endpoint.startswith('/user-agent'):
        response = user_agent(header)
    else:
        response = b"HTTP/1.1 404 Not Found\r\n\r\n"

    conn.send(response)

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        conn, _ = server_socket.accept()  # wait for client
        thread = Thread(target=process_connection, args=[conn])
        thread.start()

if __name__ == "__main__":
    main()
