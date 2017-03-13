from sense_hat import SenseHat
import time
import math

sense = SenseHat()
sense.set_rotation(180)

WIDTH     = 8
HEIGHT    = 8
SIZE      = WIDTH * HEIGHT
INTENSITY = 255
d         = [(0,0,0)];

msleep = lambda n: time.sleep(n / 1000)

START = time.clock();

def clear(update = None):
    global d
    global sense

    if update is None:
        update = False

    d = [(0,0,0)] * SIZE

    if update:
        sense.set_pixels(d)

clear()

try:
    while True:
        c = (time.clock() - START) * 10
        for x in range(WIDTH):
            for y in range(HEIGHT):
                v = 0

                v += math.sin(x * 5.0 + c)
                v += math.sin(0.5*(x*math.sin(c/2.0) + y*math.cos(c/3.0))+c)
                v += math.sin(0.5*(x*math.sin(c/2.0)))

                cx = x+0.5*math.sin(c/5.0)
                cy = y+0.5*math.cos(c/3.0)
                v += math.sin(math.sqrt(1*(math.pow(cx, 2.0)+math.pow(cy, 2.0))+1.0)+c)
                v = (v+3.0)/6.0

                r = int(abs(INTENSITY * math.sin(v*math.pi)))
                g = int(abs(INTENSITY * math.sin(v*math.pi+2.0 * math.pi/3.0)))
                b = int(abs(INTENSITY * math.sin(v*math.pi+4.0 * math.pi/3.0)))

                i = y * WIDTH + x            
                d[i] = (r,g,b)

        sense.set_pixels(d)
        msleep(25)

finally:
    clear(True)