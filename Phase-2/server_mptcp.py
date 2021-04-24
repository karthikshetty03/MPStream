import argparse, socket, cv2, utils
from datetime import datetime


def startServer(host, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.setsockopt(socket.SOL_TCP, 42, 1)
    # Bind to the port
    s.bind(("0.0.0.0", port))
    # Now wait for client connection.
    s.listen()

    print("Server listening....")

    # Establish connection with client.
    conn, addr = s.accept()
    print("Got connection from", addr)

    # try to open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        conn.close()
        raise IOError("Cannot open webcam")

    starttime = datetime.now()
    print("Starting Video Streaming at ", starttime)

    # Server side video streaming algorithm
    # Send frames from server
    count = 0
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        conn.sendall(utils.encodeNumPyArray(frame))
        count = count + 1
        if count == 100:
            break
    cap.release()
    cv2.destroyAllWindows()
    endtime = datetime.now()
    print("Ending video streaming at ", endtime)
    print("Frames Sent ", count)
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send and receive over MP-TCP")
    parser.add_argument(
        "host", help="interface the server listens at;" " host the client sends to"
    )
    parser.add_argument(
        "-p", metavar="PORT", type=int, default=6000, help="TCP port (default 6000)"
    )
    args = parser.parse_args()
    startServer(args.host, args.p)
