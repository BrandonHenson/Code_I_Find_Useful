import mouse
import random

for i in range(1, 30):
    r1 = random.randint(0, 2000)
    mouse.move(r1, r1, True, .08)
