# Network Programming Lab 1

**Student ID:** 6714951033

## Project Description

This project demonstrates basic network programming using Python.
The project implements TCP and UDP socket communication between
a client and a server.

## 1. TCP Echo Server

The TCP Echo Server demonstrates reliable communication using TCP.

### Files

- `tcp_echo_server/server.py` - TCP Echo Server
- `tcp_echo_server/client.py` - TCP Client

### Test Result

The TCP client successfully connected to the server and sent
messages. The server received the messages and returned them
to the client using the Echo mechanism.

Example:

```text
You: Hello TCP
Server: Echo: Hello TCP

You: Computer Engineering
Server: Echo: Computer Engineering