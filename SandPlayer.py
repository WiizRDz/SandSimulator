import pygame, random
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption("Sand")

if (True):
	black = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	green = (0,255,0)
	dark_green = (30,140,47)
	blue = (0,0,255)
	cyan = (11,147,215)
	brown = (83,67,27)
	yellow = (255,255,0)
	gray = (150, 150, 150)

sandl = []
barl = []
clock = pygame.time.Clock()
board = [[0]*200 for i in range(150)]
board[149] = [1]*200
for i in range(0,149):
	board[i][0] = 1
	board[i][199] = 1
r = v = random.randint(10,245)
g = n = random.randint(10,245)
b = m = random.randint(10,245)
r1 = 1
g1 = 0
b1 = 1
rg1 = 0
gg1 = 1
bg1 = 0
rg = 250
gg = 250
bc = 250
x1 = 100
y1 = 500
xp1 = x1%15
xm1 = (x1-xp1)/15
yp1 = y1%15
ym1 = (y1-yp1)/15
xm1 = int(round(xm1,0))
ym1 = int(round(ym1,0))
jump = []

while (True):
	clock.tick(60)
	screen.fill((rg,gg,bc))

	if (True):
		if (rg > 253):
			rg1 = 0
		if (rg < 240):
			rg1 = 1	
		if (rg1 == 1):
			rg = rg + .05			
		if (rg1 == 0):
			rg = rg - .05
		if (gg > 253):
			gg1 = 0
		if (gg < 240):
			gg1 = 1
		if (gg1 == 1):
			gg = gg + .1	
		if (gg1 == 0):
			gg = gg - .1	
		if (bc > 253):
			bg1 = 0		
		if (bc < 240):
			bg1 = 1		
		if (bg1 == 1):
			bc = bc + .15	
		if (bg1 == 0):
			bc = bc - .15
	
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
		
		def Fall(self):
			self.x += self.velox
			if self.velox > 0:
				self.velox -= .01
			if self.velox < 0 :
				self.velox += .01
			if abs(self.velox) < 0.2:
				self.velox = 0
			self.x = int(round(self.x,0))
			if self.yf < 149 and 0 < self.x < 199:
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
				
			self.yf = int(round(self.y,0))
			
			pygame.draw.rect(screen, self.colour, (self.x*5,self.yf*5,5,5),0)
			
	class Barrier():
		def __init__(self):
			self.x = int(xm)
			self.y = int(ym)
			
		def ShowBarrier(self):
			board[self.y][self.x] = 1
			board[self.y+1][self.x+1] = 1
			board[self.y+1][self.x] = 1
			board[self.y+1][self.x-1] = 1
			board[self.y][self.x+1] = 1
			board[self.y][self.x-1] = 1
			board[self.y-1][self.x+1] = 1
			board[self.y-1][self.x] = 1
			board[self.y-1][self.x-1] = 1			
			pygame.draw.rect(screen, black, (self.x*5-5,self.y*5-5,15,15),0)
			
	class Player():			
		def Move(self):
			try:
				board[self.y][self.x] = 1
			except AttributeError:
				pass
			self.x = int(xm1)
			self.y = int(ym1)
			board[self.y][self.x] = 0
			pygame.draw.rect(screen, cyan, (self.x*5,self.y*5,5,5), 0)
			
	pygame.draw.rect(screen, (v,n,m), (0,745,1000,5),0)
	pygame.draw.rect(screen, (v,n,m), (0,0,5,1000),0)
	pygame.draw.rect(screen, (v,n,m), (995,0,5,1000),0)
	
	xa, ya = pygame.mouse.get_pos()
	
	xp = xa%5
	xm = (xa-xp)/5
	yp = ya%5
	ym = (ya-yp)/5
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w] and len(jump) < 30:
		y1 = y1 - 7.5
		jump.append(.2)
		
	if  board[ym1-1][xm1] == 1:
		jad = 30-len(jump)
		for i in range(0,jad):
			jump.append(.2)
				
	if keys[pygame.K_d] and board[ym1][xm1+1] != 1:
		x1 = x1+ 7.5
				
	if keys[pygame.K_a] and board[ym1][xm1-1] != 1:
		x1 = x1 - 7.5
	
	if len(jump) > 0 and board[ym1+1][xm1] != 1:
		for i in range(0,len(jump)):
			c = jump[i]
			y1 += c/len(jump)*15
		
	if board[ym1+1][xm1] != 1 and len(jump) == 0:
		y1 += 15
			
	if board[ym1+1][xm1] == 1:
		jump = []
		
	xp1 = x1%15
	xm1 = (x1-xp1)/15
	yp1 = y1%15
	ym1 = (y1-yp1)/15
	xm1 = int(round(xm1,0))
	ym1 = int(round(ym1,0))
	
	if pygame.mouse.get_pressed()[2]:
		bar = Barrier()
		barl.append(bar)
	
	if pygame.mouse.get_pressed()[0]:
		sand = Sand()
		sandl.append(sand)
		sand = Sand()
		sandl.append(sand)
		
	for i in range(0,len(sandl)):
		try:
			sandl[i].Fall()
		except IndexError:
			pass
			
	for i in range(0,len(barl)):
		try:
			barl[i].ShowBarrier()
		except IndexError:
			pass
	
	play = Player()
	play.Move()
	
	pygame.display.flip()
	event = pygame.event.poll()
	if (event.type == pygame.QUIT):
		board = [[0]*200 for i in range(150)]
		board[149] = [1]*200
		for i in range(0,149):
			board[i][0] = 1
			board[i][199] = 1
		sandl = []
		barl = []
