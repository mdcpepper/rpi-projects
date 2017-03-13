from sense_hat import SenseHat
import time
import math

sense = SenseHat()
sense.set_rotation(180)

msleep = lambda n: time.sleep(n / 1000)

START = time.clock()

# A matrix
class Matrix:
    def __init__(self, w, h):
        self.width  = w
        self.height = h
        self.size   = w * h
        self.data   = [(0,0,0)] * self.size

    def set_pixel(self, x, y, rgb):
        self.data[y*self.width+x] = rgb

    def get_pixel(self, x, y):
        return self.data[y*self.width+x]

    def get_pixels(self):
        return self.data

    def clear(self):
        self.data = [(0,0,0)] * self.size

matrix = Matrix(8, 8)

try:
    while True:
        c = (time.clock() - START) * 10
        for x in range(matrix.width):
            for y in range(matrix.height):
                v = 0

                v += math.sin(x * 5.0 + c)
                v += math.sin(0.5*(x*math.sin(c/2.0) + y*math.cos(c/3.0))+c)

                cx = x+0.5*math.sin(c/5.0)
                cy = y+0.5*math.cos(c/3.0)
                v += math.sin(math.sqrt(1*(math.pow(cx, 2.0)+math.pow(cy, 2.0))+1.0)+c)
                v = (v+3.0)/6.0

                r = int(abs(255 * math.sin(v*math.pi)))
                g = int(abs(255 * math.sin(v*math.pi+2.0 * math.pi/3.0)))
                b = int(abs(255 * math.sin(v*math.pi+4.0 * math.pi/3.0)))

                matrix.set_pixel(x, y, (r, g, b))

        sense.set_pixels(matrix.get_pixels())
        msleep(10)
finally:
    matrix.clear()
    sense.set_pixels(matrix.get_pixels())