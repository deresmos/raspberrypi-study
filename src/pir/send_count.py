import json

from websocket import create_connection


def send_to_websocket(count):
    ws = create_connection("ws://localhost:8008/websocket")

    payload = json.dumps({"count": count})
    ws.send(payload)

    ws.close()


if __name__ == "__main__":
    send_to_websocket(14)
