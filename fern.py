import random
import stddraw

n = 500000
x,y = 0,0
xn,yn = x,y

stddraw.setPenRadius(0.001)
stddraw.setPenColor(stddraw.GREEN)

for i in range(n):
    r = random.randrange(0, 101)
    if r <= 2:
        x = 0.5
        y = 0.27*y
               
    elif r > 2 and r <= 15:
        x = (0.17 * xn - 0.21 * yn + 0.41)
        y = (0.22 * xn + 0.18 * yn + 0.09)
        
    elif r > 15 and r <= 30:
        x = (-0.14 * xn + 0.26 * yn + 0.57)
        y = (0.25 * xn + 0.22 * yn - 0.04)
        
    elif r > 30 and r <= 100:
        x = (0.78 * xn + 0.03 * yn + 0.11)
        y = (-0.03 * xn + 0.74 * yn + 0.27)
    
    stddraw.point(x, y)
    xn, yn = x, y
stddraw.show()