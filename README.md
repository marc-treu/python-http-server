# Codecreafter Python HTTP Server

A lightweight HTTP server implementation in Python using sockets and threading. This project demonstrates handling basic HTTP requests and responses from scratch, without relying on frameworks like Flask or Django.

## Features

* **Root Endpoint** (`/`)

  * Responds with a simple `200 OK` message.

* **Echo Endpoint** (`/echo/<message>`)

  * Returns the `<message>` part of the URL as plain text.

* **User-Agent Endpoint** (`/user-agent`)

  * Extracts and returns the `User-Agent` header sent by the client.

* **404 Handling**

  * Any unrecognized endpoint returns `404 Not Found`.

* **Multi-threaded Handling**

  * Each client connection is processed in its own thread for concurrency.

## Requirements

* Python 3.7+

No external dependencies are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/codecreafter-http-server.git
cd codecreafter-http-server
```

## Usage

Run the server:

```bash
python main.py
```

The server will start listening on `localhost:4221`.

### Example Requests

* **Root**

  ```bash
  curl http://localhost:4221/
  ```
* **Echo**

  ```bash
  curl http://localhost:4221/echo/hello
  ```
* **User-Agent**

  ```bash
  curl -H "User-Agent: CustomAgent" http://localhost:4221/user-agent
  ```

## Code Structure

* **main.py**

  * Implements all server logic, including:

    * Request reading and parsing
    * Response construction
    * Threaded connection handling

## Limitations

* Minimal HTTP compliance (only handles simple GET-like requests)
* No persistent connections or advanced HTTP features
* No SSL/TLS support

