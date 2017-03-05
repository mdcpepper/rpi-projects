from sense_hat import SenseHat
from random    import randint
from time      import sleep

sense = SenseHat()

WIDTH  = 8
HEIGHT = 8
CLEAR  = False
SPEED  = 10 # smaller is faster

msleep = lambda x: sleep(x / 1000)

sense.clear()

while True:
    x = randint(0, WIDTH-1)
    y = randint(0, HEIGHT-1)
    r = randint(80, 255)
    g = randint(80, 255)
    b = randint(80, 255)
    sense.set_pixel(x, y, r, g, b)
    msleep(SPEED)
    if CLEAR:
        sense.clear()
    
