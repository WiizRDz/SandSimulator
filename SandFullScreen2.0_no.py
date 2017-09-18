import pygame, random, math
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Sand")
pygame.font.init()
pygame.init()

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
barl = []
clock = pygame.time.Clock()
board = [[0]*math.ceil(screen.get_width()/5) for i in range(math.ceil(screen.get_height()/5))]
board[math.ceil(screen.get_height()/5)-1] = [1]*math.ceil(screen.get_width()/5)
for i in range(0,math.ceil(screen.get_height()/5)-1):
	board[i][0] = 1
	board[i][math.ceil(screen.get_width()/5)-1] = 1
	
bn = board[:]
r = random.randint(10,245)
g = random.randint(10,245)
b = random.randint(10,245)
r1 = 1
g1 = 0
b1 = 1
rg1 = 0
gg1 = 1
bg1 = 0
rg = 250
gg = 250
bc = 250

while (True):
	clock.tick(60)
	screen.fill(white)
	if clock.get_fps() < 59:
		pygame.draw.rect(screen, (140,140,0), (0,0,100,100),0)
	
	if (pygame.mouse.get_pressed()[0]):
		if (r > 253):
			r1 = 0	
		if (r < 2):
			r1 = 1		
		if (r1 == 1):
			r = r + .15			
		if (r1 == 0):
			r = r - .15
		if (g > 253):
			g1 = 0		
		if (g < 2):
			g1 = 1		
		if (g1 == 1):
			g = g + .1		
		if (g1 == 0):
			g = g - .1	
		if (b > 253):
			b1 = 0		
		if (b < 2):
			b1 = 1
		if (b1 == 1):
			b = b + .05
		if (b1 == 0):
			b = b - .05
	
	class Sand():
		def __init__(self):
			self.colour = (r,g,b)
			self.velox = 0
			while (abs(self.velox) < .5):
				self.velox = random.randint(-48,48)/80
			self.x = xm
			self.y = ym
			self.yf = int(self.y)
		
		def ID(self,ID):
			self.ID = ID
		
		def Fall(self):
			board[int(round(self.yf,0))][int(round(self.x,0))] = 0
			self.x += self.velox
			if self.velox > 0:
				self.velox -= .01
			if self.velox < 0 :
				self.velox += .01
			if abs(self.velox) < 0.2:
				self.velox = 0
			self.x = int(round(self.x,0))
			if self.yf < (math.ceil(screen.get_height()/5)-1) and 0 < self.x < (math.ceil(screen.get_width()/5)-1):
				board[self.yf][self.x] = 1
			if board[self.yf+1][self.x] != 1:
				board[self.yf][self.x] = 0
				self.y += 1
				
			if board[self.yf+1][self.x] == 1 and board[self.yf+1][self.x+1] != 1 and board[self.yf+1][self.x-1] != 1 and board[self.yf][self.x+1] != 1 and board[self.yf][self.x-1] != 1:
				board[self.yf][self.x] = 0
				self.d = random.randint(0,1)
				if self.d == 0:
					self.x += 1
				else:
					self.x -= 1
			
			if board[self.yf+1][self.x] == 1 and board[self.yf+1][self.x+1] != 1 and board[self.yf+1][self.x-1] == 1 and board[self.yf][self.x+1] != 1 and board[self.yf][self.x-1] != 1:
				board[self.yf][self.x] = 0
				self.x += 1
				
			if board[self.yf+1][self.x] == 1 and board[self.yf+1][self.x+1] == 1 and board[self.yf+1][self.x-1] != 1 and board[self.yf][self.x+1] != 1 and board[self.yf][self.x-1] != 1:
				board[self.yf][self.x] = 0
				self.x -= 1
				
			if board[self.yf+1][self.x] == 1 and board[self.yf+1][self.x+1] != 1 and board[self.yf+1][self.x-1] == 1 and board[self.yf][self.x+1] != 1 and board[self.yf][self.x-1] == 1:
				board[self.yf][self.x] = 0
				self.x += 1
				
			if board[self.yf+1][self.x] == 1 and board[self.yf+1][self.x+1] == 1 and board[self.yf+1][self.x-1] != 1 and board[self.yf][self.x+1] == 1 and board[self.yf][self.x-1] != 1:
				board[self.yf][self.x] = 0
				self.x -= 1
				
			if board[self.yf+1][self.x] == 1 and board[self.yf+1][self.x+1] == 1 and board[self.yf+1][self.x-1] == 1:
				del sandl[sandl.index(self.ID)]
				
			self.yf = int(round(self.y,0))
			
			#pygame.draw.rect(screen, self.colour, (self.x*5,self.yf*5,5,5),0)
			board[self.yf][self.x] = 1
			
	class Barrier():
		def __init__(self):
			self.x = int(xm)
			self.y = int(ym)
			try:
				board[self.y][self.x] = 1
				board[self.y+1][self.x+1] = 1
				board[self.y+1][self.x] = 1
				board[self.y+1][self.x-1] = 1
				board[self.y][self.x+1] = 1
				board[self.y][self.x-1] = 1
				board[self.y-1][self.x+1] = 1
				board[self.y-1][self.x] = 1
				board[self.y-1][self.x-1] = 1
			except IndexError:
				pass
			
		def ShowBarrier(self):
			pygame.draw.rect(screen, (abs(r-40),abs(g-40),abs(b-40)), (self.x*5-5,self.y*5-5,15,15),0)
	
	xa, ya = pygame.mouse.get_pos()
	
	xp = xa%5
	xm = (xa-xp)/5
	yp = ya%5
	ym = (ya-yp)/5
	
	if pygame.mouse.get_pressed()[2]:
		bar = Barrier()
		barl.append(bar)
	
	if pygame.mouse.get_pressed()[0]:
		sand = Sand()
		sandl.append(sand)
		sand.ID(sand)
		sand = Sand()
		sandl.append(sand)
		sand.ID(sand)
		
	for i in range(0,len(sandl)):
		try:
			sandl[i].Fall()
		except IndexError:
			pass
	
	for i in range(0,math.ceil(screen.get_height()/5)):
		for c in range(0,math.ceil(screen.get_width()/5)):
			if board[i][c] == 1:
				pygame.draw.rect(screen, (r,g,b), (c*5,i*5,5,5),0)
			
	for i in range(0,len(barl)):
		try:
			barl[i].ShowBarrier()
		except IndexError:
			pass
	
	pygame.draw.rect(screen, (r,g,b), (0,screen.get_height()-5,screen.get_width(),5),0)
	pygame.draw.rect(screen, (r,g,b), (0,0,5,screen.get_width()),0)
	pygame.draw.rect(screen, (r,g,b), (screen.get_width()-5,0,5,screen.get_height()),0)
	
	pygame.display.flip()
	event = pygame.event.poll()
	if pygame.key.get_pressed()[pygame.K_DELETE]:
		board = [[0]*math.ceil(screen.get_width()/5) for i in range(math.ceil(screen.get_height()/5))]
		board[math.ceil(screen.get_height()/5)-1] = [1]*math.ceil(screen.get_width()/5)
		for i in range(0,math.ceil(screen.get_height()/5)-1):
			board[i][0] = 1
			board[i][math.ceil(screen.get_width()/5)-1] = 1
		sandl = []
		barl = []
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		break

