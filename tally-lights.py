import board
import neopixel
import socket

HOST = "198.18.10.15"
PORT = 8099
pixels = neopixel.NeoPixel(board.D18, 24, auto_write=False)
pixels.fill((30,15,00))
pixels.show()


def show_red(ind):
    start = 8 * ind
    end = start + 8
    for i in range(start, end):
        pixels[i] = (25, 0, 0)
    pixels.show()


def show_green(ind):
    start = 8 * ind
    end = start + 8
    for i in range(start, end):
        pixels[i] = (0, 0, 25)
    pixels.show()


def clear(ind):
    start = 8 * ind
    end = start + 8
    for i in range(start, end):
        pixels[i] = (0, 0, 0)
    pixels.show()


def update(status, ind):
    if status == b'0':
        clear(ind)
    elif status == b'1':
        show_red(ind)
    elif status == b'2':
        show_green(ind)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'SUBSCRIBE TALLY\r\n')

while True:
    data = s.recv(1024)
    if data[:8] == b'TALLY OK':
        cam1 = data[9:10]
        cam6 = data[14:15]
        cam2  = data[10:11]
        update(cam2, 0)
        update(cam6, 1)
        update(cam1, 2)
    else:
        pixels.fill((30,15,00))
        pixels.show()
        print("Lost connection")

