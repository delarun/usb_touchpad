import serial,time
from pynput.mouse import Button, Controller

mouse = Controller()

serialPort = serial.Serial(
    port="COM4", baudrate=230400, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE
)

serialString = ""
x = 0
y = 0
s = 0
old_x = 0
old_y = 0
old_s = 0

while 1:
    if serialPort.in_waiting > 0:
        serialString = serialPort.readline()
        try:
            cleaned = serialString.decode("Ascii")
            out = cleaned.split(":")
            out[2] = out[2].split("\r")[0]
            x = int(out[1])*3
            y = (int(out[2]) * -1)*3
            s = int(out[0])
        except UnicodeError:
            pass

        if (old_s != s):
            if (s == 9):
                mouse.click(Button.left, 1)
                print(f"click: {s} : left")
                pass
            elif (s == 10):
                mouse.click(Button.right, 1)
                print(f"click: {s} : right")
            elif (s == 57 or s == 41 or s == 25):
                mouse.press(Button.left)
            elif (s == 56 or s == 40 or s == 24):
                mouse.release(Button.left)
            old_s = s
        if (old_x != x or old_y != y):
            print(f"s:{s},x:{x},y:{y}")
            mouse.move(x,y)
            old_x = x
            old_y = y