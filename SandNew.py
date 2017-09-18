import pygame, random
screen = pygame.display.set_mode((1000,750))
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
board = [[0]*200 for i in range(150)]
board[149] = [1]*200
for i in range(0,149):
	board[i][0] = 1
	board[i][199] = 1
r = random.randint(10,245)
g = random.randint(10,245)
b = random.randint(10,245)
r1 = 1
g1 = 0
b1 = 1


while (True):
	clock.tick(45)
	screen.fill(white)
	
	#Colour change
	if (True):
		#red
		if (True):
			if (r > 253):
				r1 = 0
			
			if (r < 2):
				r1 = 1
				
			if (r1 == 1):
				r = r + .15
				
			if (r1 == 0):
				r = r - .15
		
		#green
		if (True):
			if (g > 253):
				g1 = 0
			
			if (g < 2):
				g1 = 1
			
			if (g1 == 1):
				g = g + .1
			
			if (g1 == 0):
				g = g - .1
		
		#blue
		if (True):	
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
			self.velod = random.randint(1,2)
			self.velox = 0
			while (abs(self.velox) < .5):
				self.velox = random.randint(-48,48)/80
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
			
	pygame.draw.rect(screen, black, (0,745,1000,5),0)
	pygame.draw.rect(screen, black, (0,0,5,1000),0)
	pygame.draw.rect(screen, black, (995,0,5,1000),0)
	
	xa, ya = pygame.mouse.get_pos()
	
	xp = xa%5
	xm = (xa-xp)/5
	yp = ya%5
	ym = (ya-yp)/5
	
	if pygame.mouse.get_pressed()[0]:
		sand = Sand()
		sandl.append(sand)
		sand.ID()
		
	sandr2 = sandr
		
	for i in range(0,len(sandl)):
		try:
			sandl[i].Fall()
		except IndexError:
			pass			
	
	pygame.display.flip()
	event = pygame.event.poll()
	if (event.type == pygame.QUIT):
		break
