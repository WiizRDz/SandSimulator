import pygame, random, os
screen = pygame.display.set_mode((150,100))
pygame.display.set_caption("Sand")
pygame.font.init()
pygame.init()

#Colours
if (True):
	black = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	green = (0,255,0)
	dark_green = (30,140,47)
	blue = (0,0,255)
	brown = (83,67,27)
	yellow = (255,255,0)
	gray = (150, 150, 150)

sandl = []
sandr = []
clock = pygame.time.Clock()
board = [[0]*30 for i in range(20)]
board[19] = [1]*29
for i in range(0,19):
	board[i][0] = 1
	board[i][29] = 1
r = 0
g = 0
b = 0

while (True):
	clock.tick(10)
	screen.fill(white)
	os.system('cls')
	for i in range(0,20):
		print (board[i])
	
	class Sand():
		def __init__(self):
			self.colour = (r,g,b)
			self.velox = 0
			while (abs(self.velox) < .5):
				self.velox = random.randint(-24,24)/40
			self.x = xm
			self.y = ym
			self.yf = int(self.y)
		
		def ID(self):
			self.loc = sandl.index(sand)
		
		def Fall(self):
			self.x += self.velox
			if self.velox > 0:
				self.velox -= .01
			if self.velox < 0 :
				self.velox += .01
			if abs(self.velox) < 0.2:
				self.velox = 0
			self.x = int(round(self.x,0))
			if self.yf < 19 and 0 < self.x < 29:
				board[self.yf][self.x] = 1
			if board[self.yf+1][self.x] != 1:
				board[self.yf][self.x] = 0
				self.y += .8
			self.yf = int(round(self.y,0))
			
			pygame.draw.rect(screen, self.colour, (self.x*5,self.yf*5,5,5),0)
			
	
	xa, ya = pygame.mouse.get_pos()
	
	xp = xa%5
	xm = (xa-xp)/5
	yp = ya%5
	ym = (ya-yp)/5
	
	print (xm,ym)
	
	if pygame.mouse.get_pressed()[0]:
		sand = Sand()
		sandl.append(sand)
		sand.ID()
		
	sandr2 = sandr
		
	for i in range(0,len(sandl)):
		sandl[i].Fall()				
	
	pygame.display.flip()
	event = pygame.event.poll()
	if (event.type == pygame.QUIT):
		break
