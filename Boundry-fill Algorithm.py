import pygame
import sys, time
import math

pygame.init()
pygame.display.set_caption("Scan line Algorithm")
sys.setrecursionlimit(1000000000)
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
 
def to_pygame(coords, height):
    return (coords[0], height - coords[1])

x1, y1 = 100,500
lis = [x1,y1]
x1, y1 = to_pygame(lis, 600)
print x1,y1
x2, y2 = 200,500
lis2 = [x2,y2]
x2, y2 = to_pygame(lis2, 600)
print x2, y2
x3, y3 = 200,400
lis3 = [x3,y3]
x3, y3 = to_pygame(lis3, 600)
print x3, y3
x4, y4 = 100,400
lis4 = [x4,y4]
x4, y4 = to_pygame(lis4, 600)
print x4,y4
dx, dy = x2-x1,y2-y1

####### Color #######
def dda_line(x1,x2,y1,y2):
	x = float(x1)
	y = float(y1)

	if(abs(dx) > abs(dy)):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xI = dx/float(steps)
	yI = dy/float(steps)
	
	screen.set_at((int(math.ceil(x)), int(math.ceil(y))), (0,0,0))
	pygame.display.update()
	for k in range(0,steps):
		x=x+xI
		y=y+yI
		screen.set_at((int(math.ceil(x)), int(math.ceil(y))), (0,0,0))
		time.sleep(0.001)
		pygame.display.update()

mx = (x1+x3)/2
my = (y1+y3)/2

def boundary_fill(mx,my):
	if screen.get_at((mx,my)) == fcol:
		return
	if((mx == x1 or mx == x2) or (my == y2 or my ==y3)):
		return
	screen.set_at((mx, my), fcol)
	pygame.display.update()

	boundary_fill(mx-1,my)
	boundary_fill(mx+1,my)
	boundary_fill(mx,my-1)
	boundary_fill(mx,my+1)

fcol = (0, 0, 255, 255)
dcol = (255, 255, 255, 255)

dda_line(x1,x2,y1,y2)
dx, dy = x3-x2,y3-y2
dda_line(x2,x3,y2,y3)
dx, dy = x4-x3,y4-y3
dda_line(x3,x4,y3,y4)
dx, dy = x1-x4,y1-y4
dda_line(x4,x1,y4,y1)
boundary_fill(mx,my)
#print x1,x2,y1,y4
#fill_color(x1,x2,y1,y4)
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()